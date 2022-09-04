from gui.DPGW.BaseView import BaseView
from dataclasses import dataclass
from gui.DPGW.BaseView import BaseView
from gui.DPGW.Container import Container
from gui.DPGW.Text import Text
from gui.DPGW.Row import Row
from gui.DPGW.Button import Button
from gui.DPGW.Input import Input
import dearpygui.dearpygui as dpg


@dataclass
class MyView(BaseView):
    totalNumOfTasks: int = 0
    todoHeight = 50

    def __post_init__(self):
        self.id = self.getId()
        with dpg.stage(tag=f"Stage_{self.id}"):
            self.top = Container(
                **{
                    "tag": f"top_{self.id}",
                    "show": True,
                    "w": -1,  # -1 is full, 0 is default, .001 to 1 is multiplied to screenWidth, 1.001+ = pixel values
                    "h": -1,  # -1 is full, 0 is default, .001 to 1 is multiplied to screenHeight, 1.001+ = pixel values
                    "autoSizeX": False,  # Overtakes w
                    "autoSizeY": False,  # Overtakes h
                    "itemOrientation": "col",  # row = items stacked left to right, col = items stacked top to btm
                    "horzGap": 0,  # space between items when itemOrientation is row
                    "verticalItemSpacing": [0, 20],
                    "border": True,
                    "borderRadius": 0,
                    "borderColor": [255, 0, 0, 0],  # "orange",
                    "bkgColor": [0, 0, 255, 5],
                    "padding": [30, 30],  # [LR,TB] !Can also be negative
                    "onHover": None,
                    "noScrollBar": True,
                    "font": None,  # "main_20"
                }
            ).create()

            self.title = Text(
                **{
                    "tag": f"Title_{self.id}",
                    "w": 0,  # 0 is default
                    "h": 0,  # 0 is default
                    "color": [255, 255, 255, 255],
                    "text": "Todo App",
                    "bullet": False,
                    "font": "mainFont_50",
                }
            ).create(Parent=self.top.link())

            self.createNewTodoComponents()
            self.todoItemsContainer = Container(
                **{
                    "tag": f"todoItemsContainer_{self.id}",
                    "show": True,
                    "w": -1,  # -1 is full, 0 is default, .001 to 1 is multiplied to screenWidth, 1.001+ = pixel values
                    "h": 2,  # -1 is full, 0 is default, .001 to 1 is multiplied to screenHeight, 1.001+ = pixel values
                    "autoSizeX": False,  # Overtakes w
                    "autoSizeY": False,  # Overtakes h
                    "itemOrientation": "col",  # row = items stacked left to right, col = items stacked top to btm
                    "horzGap": 0,  # space between items when itemOrientation is row
                    "verticalItemSpacing": [0, 5],
                    "border": True,
                    "borderRadius": 0,
                    "borderColor": [255, 0, 255, 0],  # "orange",
                    "bkgColor": [0, 0, 255, 0],
                    "padding": [0, 0],  # [LR,TB] !Can also be negative
                    "onHover": None,
                    "noScrollBar": True,
                    "font": None,  # "main_20"
                }
            ).create(Parent=self.top.link())
            

            self.createNotificationsRow()

    def createNotificationsRow(self):

        self.notificationRow = Row(
            **{
                "tag": f"notificationRow_{self.id}",
                "parent": self.top.link(),
                "numCols": 2,
                "sizing": 0,  # ,1,2,3,
                "border": False,  # True,
                "bkgColor": [255, 0, 0, 0],
                "padding": [0, 20],  # Default is [10,0]
            }
        ).create()

        textContainer = Container(
            **{
                "tag": f"textContainer_{self.id}",
                "show": True,
                "w": 0,  # -1 is full, 0 is default, .001 to 1 is multiplied to screenWidth, 1.001+ = pixel values
                "h": 50,  # -1 is full, 0 is default, .001 to 1 is multiplied to screenHeight, 1.001+ = pixel values
                "autoSizeX": False,  # Overtakes w
                "autoSizeY": False,  # Overtakes h
                "itemOrientation": "col",  # row = items stacked left to right, col = items stacked top to btm
                "horzGap": 0,  # space between items when itemOrientation is row
                "verticalItemSpacing": [0, 0],
                "border": True,
                "borderRadius": 0,
                "borderColor": [255, 0, 0, 0],  # "orange",
                "bkgColor": [0, 0, 255, 50],
                "padding": [15, 10],  # [LR,TB] !Can also be negative
                "onHover": None,
                "noScrollBar": True,
                "font": None,  # "main_20"
            }
        ).create(Parent=self.notificationRow.link())


        self.numTasks = Text(
            **{
                "tag": f"numTasks_{self.id}",
                "color": [255, 255, 255, 255],
                "text": "You Have 0 Tasks Left",
                "bullet": False,
                "font": "mainFont_20",
            }
        ).create(Parent=textContainer.link())

        self.clearAllTasksButton = Button(
            **{
                "tag": f"clearAllTasksButton_{self.id}",
                "w": 100,
                "h": 50,
                "text": "Clear All",
                "textColor": [255, 255, 255, 255],  # "white",
                "font": "mainFont_20",
                "callback": self.clearAll,
                "border": False,
                "borderRadius": 0,
                "borderColor": [0, 0, 0, 0],  #'red',
                "bkgColor": [142, 73, 233, 255],
                "bkgColorHovered": [
                    142,
                    73,
                    233,
                    55,
                ],  # [37 * 0.7, 37 * 0.7, 38 * 0.7, 255],
                "bkgColorClicked": [0, 0, 0, 0],  #'green',
                "padding": [10, 10],  # [10, 10],
            }
        ).create(Parent=self.notificationRow.link())

    def createNewTodoComponents(self):
        self.newTodoRow = Row(
            **{
                "tag": f"newTodoRow_{self.id}",
                "parent": self.top.link(),
                "numCols": 2,
                "sizing": 0,  # ,1,2,3,
                "border": True,
                "bkgColor": [255, 0, 0, 0],
                "padding": [0, 0],  # Default is [10,0]
            }
        ).create()

        self.newTodoInput = Input(
            **{
                "tag": f"newTodoInput_{self.id}",
                "w": -1,  # 0.58,
                "h": 200,  # -1,
                "border": True,
                "borderColor": "white",
                #'borderRadius': 5,
                "padding": [10, 10],
                "bkgColor": [255, 0, 0, 0],
                # "bkgColorHovered": [37 * 0.7, 37 * 0.7, 38 * 0.7, 255],
                #'bkgColorClicked': 'green',
                "defaultValue": "",  # self.getLastModifiedFile(DOWNLOADED_VIDEOS_PATH),
                "focus": True,
                # "textColor": "red",
                "font": "mainFont_20",
                "multiLine": False,
                # "onHover": self.stopShow
                "hint": "Add Your New Todo",
            }
        ).create(Parent=self.newTodoRow.link())

        self.addNewTodoButton = Button(
            **{
                "tag": f"addNewTodoButton_{self.id}",
                "w": 100,
                "h": 0,
                "text": "Add",
                "textColor": [255, 255, 255, 255],  # "white",
                "font": "mainFont_20",
                "callback": self.createTodo,  # self.autoFind,
                "border": False,
                "borderRadius": 0,
                "borderColor": [0, 0, 0, 0],  #'red',
                "bkgColor": [142, 73, 233, 255],
                "bkgColorHovered": [
                    142,
                    73,
                    233,
                    55,
                ],  # [37 * 0.7, 37 * 0.7, 38 * 0.7, 255],
                "bkgColorClicked": [0, 0, 0, 0],  #'green',
                "padding": [10, 10],  # [10, 10],
            }
        ).create(Parent=self.newTodoRow.link())

    def createTodo(self):
        task = self.newTodoInput.getValue()
        self.newTodoInput.clear()
        
        
        # Expand the todoItems Container height 
        todoItemsContainerH = dpg.get_item_height(self.todoItemsContainer.link())
        fullH  = todoItemsContainerH + self.todoHeight + self.todoItemsContainer.verticalItemSpacing[1]
        dpg.configure_item(self.todoItemsContainer.link(), height=fullH)
    

        row = Row(
            **{
                "tag": f"todoItemRow_{self.totalNumOfTasks}_{self.id}",
                "parent": self.todoItemsContainer.link(),
                "numCols": 2,
                "sizing": 0,  # ,1,2,3,
                "border": False,#True,
                "bkgColor": [242, 242, 242, 10],
                "padding": [0, 0],  # Default is [10,0]
            }
        ).create()

        textContainer = Container(
            **{
                "tag": f"textContainer_{self.totalNumOfTasks}_{self.id}",
                "show": True,
                "w": 0,  # -1 is full, 0 is default, .001 to 1 is multiplied to screenWidth, 1.001+ = pixel values
                "h": self.todoHeight,  # -1 is full, 0 is default, .001 to 1 is multiplied to screenHeight, 1.001+ = pixel values
                "autoSizeX": False,  # Overtakes w
                "autoSizeY": False,  # Overtakes h
                "itemOrientation": "col",  # row = items stacked left to right, col = items stacked top to btm
                "horzGap": 0,  # space between items when itemOrientation is row
                "verticalItemSpacing": [0, 0],
                "border": True,
                "borderRadius": 0,
                "borderColor": [255, 0, 0, 0],  # "orange",
                "bkgColor": [0, 0, 255, 50],
                "padding": [15, 10],  # [LR,TB] !Can also be negative
                "onHover": None,
                "noScrollBar": True,
                "font": None,  # "main_20"
            }
        ).create(Parent=row.link())

        text = Text(
            **{
                "tag": f"todoItemText_{self.totalNumOfTasks}_{self.id}",
                "color": "white",
                "text": task,
                "bullet": False,
                "font": "mainFont_20",
            }
        ).create(Parent=textContainer.link())

        delTodo = Button(
            **{
                "tag": f"delTodoButton_{self.totalNumOfTasks}_{self.id}",
                "w": 100,
                "h": self.todoHeight,
                "text": "Del",
                "textColor": [255, 255, 255, 255],  # "white",
                "font": "mainFont_20",
                "callback": self.deleteTodo,
                "user_data": row.tag + "_table",
                "border": False,
                "borderRadius": 0,
                "borderColor": [0, 0, 0, 0],  #'red',
                "bkgColor": [231, 77, 61, 255],
                "bkgColorHovered": [
                    231,
                    77,
                    61,
                    155,
                ],  # [37 * 0.7, 37 * 0.7, 38 * 0.7, 255],
                "bkgColorClicked": [0, 0, 0, 0],  #'green',
                "padding": [10, 10],  # [10, 10],
            }
        ).create(Parent=row.link())
        
        # Set numTasks
        self.totalNumOfTasks += 1
        self.numTasks.setValue(f"You Have {self.totalNumOfTasks} Tasks Left")

    def deleteTodo(self, sender, _, data):
        dpg.delete_item(data)
        self.totalNumOfTasks -= 1
        self.numTasks.setValue(f"You Have {self.totalNumOfTasks} Tasks Left")
        
        # Retract the todoItems Container height 
        todoItemsContainerH = dpg.get_item_height(self.todoItemsContainer.link())
        fullH  = todoItemsContainerH - self.todoHeight - self.todoItemsContainer.verticalItemSpacing[1]
        dpg.configure_item(self.todoItemsContainer.link(), height=fullH)


    def clearAll(self):
        dpg.delete_item(self.todoItemsContainer.link(), children_only=True)
        self.totalNumOfTasks = 0
        self.numTasks.setValue(f"You Have {self.totalNumOfTasks} Tasks Left")
        dpg.configure_item(self.todoItemsContainer.link(), height=2)
