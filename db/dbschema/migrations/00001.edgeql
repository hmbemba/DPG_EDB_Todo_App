CREATE MIGRATION m1tleq5wv4omp26vydtuufmhmboogph4ixnyf6p754qgg4jcttenpa
    ONTO initial
{
  CREATE TYPE default::Todos_Model {
      CREATE REQUIRED PROPERTY completed -> std::bool;
      CREATE REQUIRED PROPERTY task -> std::str;
  };
};
