#include "pykimix_c.h"
#include <stdlib.h>
#include <time.h>

// Clamp value
int clamp(int val, int min_val, int max_val) {
    if (val < min_val) return min_val;
    if (val > max_val) return max_val;
    return val;
}

// Random integer in range
int random_int(int min_val, int max_val) {
    return rand() % (max_val - min_val + 1) + min_val;
}

// Call this once in Python to seed random
void seed_random() {
    srand((unsigned int)time(NULL));
}