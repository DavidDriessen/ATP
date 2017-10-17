
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#include <pybind11/embed.h>
#pragma GCC diagnostic pop

namespace py = pybind11;

#include <iostream>

//py::object lemonator_proxy = py::module::import("Simulator.Lem_sim_interface.lemonator");


struct lemonator_proxy {
    py::object lemonator;
    py::object lcd;

    lemonator_proxy(int com, int l, int p):lemonator(py::module::import("Simulator.Lem_sim_interface.lemonator")),
    lcd(this->lemonator.attr("lcd"))
    {
    }
};

//class lemonator_proxy {
//public:
//    py::object lemonator;
//    py::object lcd;
//
//    lemonator_proxy(int com, int l, int p):lemonator(py::module::import("Simulator.Lem_sim_interface.lemonator")),
//    lcd(this->lemonator.attr("lcd"))
//    {
//    }
//};