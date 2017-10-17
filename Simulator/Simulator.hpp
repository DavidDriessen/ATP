
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#include <pybind11/embed.h>
#pragma GCC diagnostic pop

namespace py = pybind11;

#include <iostream>

#pragma GCC visibility push(hidden)
class output_proxy {
    py::object py_set;
    py::object py_write;
public:
    output_proxy(py::object p):
    py_set(p.attr("set")),
    py_write(p.attr("write"))
    {}

    void set(bool i)
    {
        py_set(i);
    }

    void operator << (const char* text){
        py_write(text);
    }
};

class lemonator_proxy {
public:
    py::object lemonator;
    output_proxy lcd;

    lemonator_proxy(int com, int l, int p):
    lemonator(py::module::import("Simulator.Lem_sim_interface.lemonator")),
    lcd(this->lemonator.attr("lcd"))
    {
    }
};
#pragma GCC visibility pop
