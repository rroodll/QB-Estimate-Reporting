"""
DISTRIBUTION STATEMENT A. Approved for public release. Distribution is unlimited.

This material is based upon work supported by the Under Secretary of Defense for
Research and Engineering under Air Force Contract No. FA8702-15-D-0001. Any opinions,
findings, conclusions or recommendations expressed in this material are those of the
author(s) and do not necessarily reflect the views of the Under Secretary of Defense
for Research and Engineering.

© 2023 Massachusetts Institute of Technology.

The software/firmware is provided to you on an As-Is basis

Delivered to the U.S. Government with Unlimited Rights, as defined in DFARS Part
252.227-7013 or 7014 (Feb 2014). Notwithstanding any copyright notice, U.S. Government
rights in this work are defined by DFARS 252.227-7013 or DFARS 252.227-7014 as detailed
above. Use of this work other than as specifically authorized by the U.S. Government
may violate any copyrights that exist in this work.
"""

import json         as   json
import jsonschema   as   schema
import pandas       as   pd




#######                             ###########################################
######   REPORTING SCHEMA          ############################################
#####                             #############################################


# See ../schema/resource_estimate_schema.json.  


# schema_resource_estimate = {
# #    "info":                  {"type" : "object"},
#     "id":                    {"type" : "string"},
#     "name":                  {"type" : "string"},
#     "category":              {"enum" : ["scientific", "industrial"]},
#     "size":                  {"type" : "string"},
#     "task":                  {"enum" : ["ground_state_energy_estimation", "time_independent_dynamics", 
#                                         "time_dependent_dynamics", "linear_system", "nonlinear_differential_equation"]},
#     "implementation":        {"type" : "string"},
#     "value":                 {"type" : "number"},
#     "value_ci":              {"type" : "array", 
#                               "items":  {
#                                   "type": "number"
#                                 }
#                               },
#     "value_per_t_gate":                        {"type" : "number"},
#     "circuit_repetitions_per_calculation":     {"type" : "number"},
#     "calculation_repetitions":                 {"type" : "number"},
#     "total_circuit_repetitions":               {"Type" : "number"},
#     "runtime_requirement":                     {"Type" : "number"},
#     "logical-abstract":      {"type" : "object",
#                               "additionalProperties" : {
#                                   "type": "object",
#                                   "required" : ["num_qubits", "t_count"],
#                                   "properties": {
#                                       "num_qubits":     {"type" : "number"},
#                                       "t_count":        {"type" : "number"},
#                                       "circuit_depth":  {"type" : "number"},
#                                       "gate_count":     {"type" : "number"},
#                                       "t_depth":        {"type" : "number"},
#                                       "clifford_count": {"type" : "number"}
#                                   }
#                               } },
#     "logical-compiled":      {"type" : "object",
#                               "additionalProperties" : {
#                                   "type": "object",
#                                   "required" : ["logical_architecture_description", "num_qubits",
#                                                 "t_count", "num_t_factories"],
#                                   "properties": {
#                                       "logical_architecture_description":     {"type" : "string"},
#                                       "num_qubits":                           {"type" : "number"},
#                                       "t_count":                              {"type" : "number"},
#                                       "num_t_factories":                      {"type" : "integer"},
#                                       "gate_count":                           {"type" : "number"},
#                                       "circuit_depth":                        {"type" : "number"},
#                                       "t_depth":                              {"type" : "number"},
#                                       "clifford_count":                       {"type" : "number"}
#                                   }
#                               } },   
#     "physical":              {"type" : "object",
#                               "additionalProperties" : {
#                                   "type": "object",
#                                   "required" : ["physical_architecture_description", "runtime",
#                                                 "num_t_factories", "num_qubits", "t_count",
#                                                 "code_name", "code_distance"],
#                                   "properties": {
#                                       "physical_architecture_description":    {"type" : "string"},
#                                       "code_name":                            {"enum" : ["surface", "other"]},
#                                       "code_distance":                        {"type" : "integer"},
#                                       "runtime":                              {"type" : "number"},
#                                       "num_qubits":                           {"type" : "number"},
#                                       "t_count":                              {"type" : "number"},
#                                       "num_t_factories":                      {"type" : "integer"},
#                                       "num_factory_qubits":                   {"type" : "integer"},
#                                       "gate_count":                           {"type" : "number"},
#                                       "circuit_depth":                        {"type" : "number"},
#                                       "t_depth":                              {"type" : "number"},
#                                       "clifford_count":                       {"type" : "number"}
#                                   }
#                               } },   
#     "required":              ["id", "name", "category", "size", "task", "implementation",
#                               "value", "logical-abstract", "value_per_t_gate", 
#                               "circuit_repetitions_per_calculation", "calculation_repetitions",
#                               "total_circuit_repetitions", "runtime_requirement"]

# }   





# resource_estimate = {
# #    "info":                  {"type" : "object"},
#     "id":                    {"type" : "string"},
#     "name":                  {"type" : "string"},
#     "category":              {"enum" : ["scientific", "industrial"]},
#     "size":                  {"type" : "string"},
#     "task":                  {"enum" : ["ground_state_energy_estimation", "time_independent_dynamics", 
#                                         "time_dependent_dynamics", "linear_system", "nonlinear_differential_equation"]},
#     "implementation":        {"type" : "string"},
#     "value":                 {"type" : "number"},
#     "repetitions":           {"type" : "integer"},
#     "logical-abstract":      {"type" : "object",
#                               "additionalProperties" : {
#                                   "type": "object",
#                                   "required" : ["num_qubits", "t_count"],
#                                   "properties": {
#                                       "num_qubits":     {"type" : "integer"},
#                                       "t_count":        {"type" : "integer"},
#                                       "circuit_depth":  {"type" : "integer"},
#                                       "gate_count":     {"type" : "integer"},
#                                       "t_depth":        {"type" : "integer"},
#                                       "clifford_count": {"type" : "integer"}
#                                   }
#                               } },
#     "logical-compiled":      {"type" : "object",
#                               "additionalProperties" : {
#                                   "type": "object",
#                                   "required" : ["logical_architecture_description", "num_qubits",
#                                                 "t_count", "num_t_factories"],
#                                   "properties": {
#                                       "logical_architecture_description":     {"type" : "string"},
#                                       "num_qubits":                           {"type" : "integer"},
#                                       "t_count":                              {"type" : "integer"},
#                                       "num_t_factories":                      {"type" : "integer"},
#                                       "gate_count":                           {"type" : "integer"},
#                                       "circuit_depth":                        {"type" : "integer"},
#                                       "t_depth":                              {"type" : "integer"},
#                                       "clifford_count":                       {"type" : "integer"}
#                                   }
#                               } },   
#     "physical":              {"type" : "object",
#                               "additionalProperties" : {
#                                   "type": "object",
#                                   "required" : ["physical_architecture_description", "runtime",
#                                                 "num_t_factories", "num_qubits", "t_count",
#                                                 "code_name", "code_distance"],
#                                   "properties": {
#                                       "physical_architecture_description":    {"type" : "string"},
#                                       "code_name":                            {"type" : "string"},
#                                       "code_distance":                        {"type" : "integer"},
#                                       "runtime":                              {"type" : "float"},
#                                       "num_qubits":                           {"type" : "integer"},
#                                       "t_count":                              {"type" : "integer"},
#                                       "num_t_factories":                      {"type" : "integer"},

#                                       "gate_count":                           {"type" : "integer"},
#                                       "circuit_depth":                        {"type" : "integer"},
#                                       "t_depth":                              {"type" : "integer"},
#                                       "clifford_count":                       {"type" : "integer"},
#                                       "num_factory_qubits":                   {"type" : "integer"}
#                                   }
#                               } },   
#     "required":              ["info", "logical-abstract"]
# }



#######                             ###########################################
######   UTILITIES                 ############################################
#####                             #############################################


def load_nested_json(filename,label=None,orient="column"):

    with open(filename) as file:
        data      =   json.load(file)   

    data_df   =   pd.json_normalize(data,max_level=2)

    data_df.columns = data_df.columns.map(lambda x: x.split(".")[-1])

    if orient == "column":
        data_df = data_df.transpose()
        if label is not None:
            data_df.columns = [label];
    else:
        if label is not None:
            data_df.rows = [label];

    return(data_df)