#include "pykimix_c.h"
#include <math.h>

// --- Rectangle collision ---
int rect_collision(double x1, double y1, double w1, double h1,
                   double x2, double y2, double w2, double h2) {
    if (x1 < x2 + w2 && x1 + w1 > x2 &&
        y1 < y2 + h2 && y1 + h1 > y2)
        return 1;
    return 0;
}

// --- Circle collision ---
int circle_collision(double x1, double y1, double r1,
                     double x2, double y2, double r2) {
    double dx = x1 - x2;
    double dy = y1 - y2;
    double dist = sqrt(dx*dx + dy*dy);
    return dist < (r1 + r2);
}