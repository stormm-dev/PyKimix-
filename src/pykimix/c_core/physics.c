#include "pykimix_c.h"
#include <math.h>

// --- Vector operations ---
Vec2 vec_add(Vec2 a, Vec2 b) {
    Vec2 res = {a.x + b.x, a.y + b.y};
    return res;
}

Vec2 vec_sub(Vec2 a, Vec2 b) {
    Vec2 res = {a.x - b.x, a.y - b.y};
    return res;
}

Vec2 vec_scale(Vec2 a, double s) {
    Vec2 res = {a.x * s, a.y * s};
    return res;
}

double vec_length(Vec2 a) {
    return sqrt(a.x * a.x + a.y * a.y);
}

Vec2 vec_normalize(Vec2 a) {
    double len = vec_length(a);
    Vec2 res = {0, 0};
    if (len != 0) {
        res.x = a.x / len;
        res.y = a.y / len;
    }
    return res;
}