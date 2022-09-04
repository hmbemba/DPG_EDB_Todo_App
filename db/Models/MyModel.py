import edgedb
from db.edbw.EdgeDBModel import EdgeDBModel
from db.edbw.Properties import Type
import pprint
pp = pprint.PrettyPrinter(indent=4)

client = edgedb.create_client()

TodosModel = EdgeDBModel(modelName='Todos_Model', client=client)
TodosModel.addProperty(_propertyName = 'task', _propertyType = Type.str, _req = True)
TodosModel.addProperty(_propertyName = 'completed', _propertyType = Type.bool, _req = True)


#InvoicesModel.getByProperty(printStr=True, propName='three_word_name', propType=Type.str, _three_word_name='TameHolographcScallop')

#InvoicesModel.insert(printStr=True, _three_word_name="hello world")

#InvoicesModel.updateEntry(uuid="123",printStr=True, title="blade runner")

#InvoicesModel.delEntry(uuid="123", printStr=True)