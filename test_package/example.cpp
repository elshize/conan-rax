#include <iostream>
extern "C" {
#include "rax.h"
}

int main() {
    rax *rt = raxNew();
    raxFree(rt);
}
