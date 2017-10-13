//
// Created by jeremy on 13-10-17.
//

#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#include "pybind11/include/pybind11/embed.h"
#pragma GCC diagnostic pop

#include <iostream>

namespace py = pybind11;

int main(){
    std::cout << "test print";
    //py::object lemonator = py::module::import("Lem_sim_interface");

    //auto lemonater = py::module::import("Lem_sim_interface");
    //auto resultobj = lemonater.attr("lemonator_sim_interface")();
//double result = resultobj.cast<double>();

    std::cout << "lemonator created";
}
