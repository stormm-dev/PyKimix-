#ifndef PYKIMIX_C_H
#define PYKIMIX_C_H

// --- Math ---
int add(int a, int b);
int sub(int a, int b);
int mul(int a, int b);
double divd(double a, double b);

// --- Vector2 ---
typedef struct {
    double x;
    double y;
} Vec2;

Vec2 vec_add(Vec2 a, Vec2 b);
Vec2 vec_sub(Vec2 a, Vec2 b);
Vec2 vec_scale(Vec2 a, double s);
double vec_length(Vec2 a);
Vec2 vec_normalize(Vec2 a);

// --- Collision ---
int rect_collision(double x1, double y1, double w1, double h1,
                   double x2, double y2, double w2, double h2);
int circle_collision(double x1, double y1, double r1,
                     double x2, double y2, double r2);

// --- Utils ---
int clamp(int val, int min_val, int max_val);
int random_int(int min_val, int max_val);

#endif