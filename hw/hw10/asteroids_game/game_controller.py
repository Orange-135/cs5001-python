from laserbeam import LaserBeam
from asteroid import Asteroid
from spaceship import Spaceship


class GameController:
    """
    Maintains the state of the game
    and manages interactions of game elements.
    """

    def __init__(self, SPACE, fadeout):
        """Initialize the game controller"""
        self.SPACE = SPACE
        self.fadeout = fadeout

        self.spaceship_hit = False
        self.asteroid_destroyed = False
        self.asteroids = [Asteroid(self.SPACE)]
        self.laser_beams = []
        self.spaceship = Spaceship(self.SPACE)

    def update(self):
        """Updates game state on every frame"""
        self.do_intersections()

        for asteroid in self.asteroids:
            asteroid.display()

        # ======================================================
        # TODO: Problem 3, Part 2: Laser beam handler
        # Your code will replace (or augment) the next several
        # lines. Laser beam objects should remain in the scene
        # as many frames as their lifespan allows.
        # Begin problem 3 code changes
        for l in range(len(self.laser_beams)-1, -1, -1):
            if self.laser_beams[l].life_span > 0:
                self.laser_beams[l].display()
            else:
                del self.laser_beams[l]

        # End problem 3, part 2 code changes
        # =======================================================

        self.spaceship.display()

        # Carries out necessary actions if game over
        if self.spaceship_hit:
            if self.fadeout <= 0:
                fill(1)
                textSize(30)
                text("YOU HIT AN ASTEROID",
                     self.SPACE['w']/2 - 165, self.SPACE['h']/2)
            else:
                self.fadeout -= 1

        if self.asteroid_destroyed:
            fill(1)
            textSize(30)
            text("YOU DESTROYED THE ASTEROIDS!!!",
                 self.SPACE['w']/2 - 250, self.SPACE['h']/2)

    def fire_laser(self, x, y, rot):
        """Add a laser beam to the game"""
        x_vel = sin(radians(rot))
        y_vel = -cos(radians(rot))
        self.laser_beams.append(
            LaserBeam(self.SPACE, x, y, x_vel, y_vel)
            )

    def handle_keypress(self, key, keycode=None):
        if (key == ' '):
            if self.spaceship.intact:
                self.spaceship.control(' ', self)
        if (keycode):
            if self.spaceship.intact:
                self.spaceship.control(keycode)

    def handle_keyup(self):
        if self.spaceship.intact:
            self.spaceship.control('keyup')

    def do_intersections(self):
        # ======================================================
        # TODO: Problem 4, Part 1: Intersections
        # Here's where you'll probably want to check for intersections
        # between asteroids and laser beams. Laser beams should be removed
        # from the scene if they hit an asteroid, and the asteroid should
        # blow up (the blow_up_asteroid method also must be written. It's
        # been started for you below).
        #
        # The intersection logic below between the spaceship
        # and asteroids should give a hint as to how this will work.
        # Begin code changes for Problem 3, Part 1: Intersections
        new_laser_beams = []
        for a, laser_beam in enumerate(self.laser_beams):
            hit = False
            for b, asteroid in enumerate(self.asteroids):
                distance = ((laser_beam.x - asteroid.x)**2 + (laser_beam.y - asteroid.y)**2)**0.5
                if distance < asteroid.radius + laser_beam.radius:
                    hit = True
                    self.blow_up_asteroid(a, b)
                    break
                new_laser_beams.append(laser_beam)
        self.laser_beams = new_laser_beams

        # End of code changes for Problem 4, Part 1: Intersections
        # ======================================================

        # If the space ship still hasn't been blown up
        if self.spaceship.intact:
            # Check each asteroid for intersection
            for i in range(len(self.asteroids)):
                if (
                      abs(self.spaceship.x - self.asteroids[i].x)
                      < max(self.asteroids[i].radius, self.spaceship.radius)
                      and
                      abs(self.spaceship.y - self.asteroids[i].y)
                      < max(self.asteroids[i].radius, self.spaceship.radius)):
                    # We've intersected an asteroid
                    self.spaceship.blow_up(self.fadeout)
                    self.spaceship_hit = True

    def blow_up_asteroid(self, a, b):
        # ======================================================
        # TODO: Problem 4, Part 2: Asteroid blow-up

        # Here you'll write the code to blow up an asteroid.
        # The parameters represent the indexes for the list of
        # asteroids and the list of laser beams, indicating
        # which asteroid is hit by which laser beam.

        # You'll need to:
        # A) Remove the hit asteroid from the scene
        # B) Add appropriate smaller asteroids to the scene
        # C) Make sure that the smaller asteroids are positioned
        #    correctly and flying off in the correct directions

        # Specifically. If the large asteroid is hit, it should
        # break into two medium asteroids, which should fly off
        # perpendicularly to the direction of the laser beam.

        # If a medium asteroid is hit, it should break into three
        # small asteroids, two of which should fly off perpendicularly
        # to the direction of the laser beam, and the third
        # should fly off in the same direction that the laser
        # beam had been traveling.

        # If a small asteroid is hit, it disappears.

        # Begin code changes for Problem 4, Part 2: Asteroid blow-up
        hit_laser_beam = self.laser_beams[a]
        blow_asteroid = self.asteroids.pop(b)

        if blow_asteroid.asize == 'Large':
            asteroid_med1 = Asteroid(self.SPACE, asize='Med', x=blow_asteroid.x, y=blow_asteroid.y, x_vel=-hit_laser_beam.x_vel/2, y_vel=hit_laser_beam.y_vel/2)
            asteroid_med2 = Asteroid(self.SPACE, asize='Med', x=blow_asteroid.x, y=blow_asteroid.y, x_vel=hit_laser_beam.x_vel/2, y_vel=-hit_laser_beam.y_vel/2)
            self.asteroids.extend([asteroid_med1, asteroid_med2])

        if blow_asteroid.asize == 'Med':
            asteroid_sm1 = Asteroid(self.SPACE, asize='Small', x=blow_asteroid.x, y=blow_asteroid.y, x_vel=-hit_laser_beam.x_vel/2, y_vel=hit_laser_beam.y_vel/2)
            asteroid_sm2 = Asteroid(self.SPACE, asize='Small', x=blow_asteroid.x, y=blow_asteroid.y, x_vel=hit_laser_beam.x_vel/2, y_vel=-hit_laser_beam.y_vel/2)
            asteroid_sm3 = Asteroid(self.SPACE, asize='Small', x=blow_asteroid.x, y=blow_asteroid.y, x_vel=hit_laser_beam.x_vel/2, y_vel=hit_laser_beam.y_vel/2)
            self.asteroids.extend([asteroid_sm1, asteroid_sm2, asteroid_sm3])

        if not self.asteroids:
            self.asteroid_destroyed = True
