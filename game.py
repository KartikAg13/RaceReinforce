import pygame, sys

def catmull_rom_spline(points, resolution = 5, loop = True):
    if loop:
        points = [points[-2], points[-1]] + points + [points[0], points[1]]
    spline_pts = []
    for i in range(1, len(points) - 2):
        p0, p1, p2, p3 = points[i-1], points[i], points[i+1], points[i+2]
        for t in range(resolution):
            t_norm = t / float(resolution)
            x = 0.5 * (
                (2 * p1[0]) +
                (-p0[0] + p2[0]) * t_norm +
                (2*p0[0] - 5*p1[0] + 4*p2[0] - p3[0]) * (t_norm**2) +
                (-p0[0] + 3*p1[0] - 3*p2[0] + p3[0]) * (t_norm**3)
            )
            y = 0.5 * (
                (2 * p1[1]) +
                (-p0[1] + p2[1]) * t_norm +
                (2*p0[1] - 5*p1[1] + 4*p2[1] - p3[1]) * (t_norm**2) +
                (-p0[1] + 3*p1[1] - 3*p2[1] + p3[1]) * (t_norm**3)
            )
            spline_pts.append((x, y))
    return spline_pts

outer_points = [(1700, 950), (300, 950), (150, 800), (300, 650), (400, 750), (300, 800), (400, 850), (500, 800), (500, 600), (400, 500), (600, 400), 
                (300, 300), (400, 200), (1000, 100), (1010, 110), (1000, 120), (900, 200), (900, 300), (800, 300), (850, 400), (925, 475), (1010, 550),
                (1100, 600), (1200, 650), (1300, 650), (1400, 750), (1400, 350), (1450, 300), (1500, 250), (1550, 300), (1600, 350), (1600, 850), (1700, 850)]

smoothed_outer = catmull_rom_spline(outer_points, resolution=5, loop=True)

pygame.init()
screen = pygame.display.set_mode((1900, 1000))
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    # Draw outer boundary
    pygame.draw.polygon(screen, (100, 100, 100), smoothed_outer)

    # Outline
    pygame.draw.polygon(screen, (255, 255, 255), smoothed_outer, 3)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
