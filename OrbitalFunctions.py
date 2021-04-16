import numpy as np
import pygame

solar_system = {"M_sun": 1.0, "G": 39.4784176043574320}


def SolarCircularVelocity(p, solar_system):

    G = solar_system["G"]
    M = solar_system["M_sun"]
    r = (p.x[0]**2 + p.x[1]**2) ** 0.5

    # return the circular velocity
    return (G*M/r)**0.5


def SolarGravitationalAcceleration(p, solar_system):

    G = solar_system["G"]
    M = solar_system["M_sun"]
    r = (p.x[0]**2 + p.x[1]**2) ** 0.5

    # accel in the AU/yr/yr
    a_grav = -1.0*G*M/r**2

    # find the angle at this position
    if p.x[0] == 0.0:
        if p.x[1] > 0:
            theta = 0.5*np.pi
        else:
            theta = 1.5*np.pi
    else:
        theta = np.arctan2(p.x[1], p.x[0])

    # set the x adn y components of the accel
    return a_grav*np.cos(theta), a_grav*np.sin(theta)


def calc_dt(p):

    # integration tol
    ETA_TIME_STEP = 0.0004

    eta = ETA_TIME_STEP

    v = (p.v[0]**2 + p.v[1]**2)**0.5
    a = (p.a_g[0]**2 + p.a_g[1]**2)**0.5
    dt = eta * np.fmin(1./np.fabs(v), 1./np.fabs(a)**0.5)

    return dt

# ------------------#
# step calculations #
# ------------------#


def x_first_step(x_i, v_i, a_i, dt):
    # x_1/2 = x_0 + (1/2)v_0 Delta_t + (1/4)a_0 Delta_t^2
    return x_i + 0.5*v_i*dt + 0.25*a_i*dt**2


def v_full_step(x_i, v_i, a_ipoh, dt):
    # v_i+1 = v_i + a_i+1/2 Delta_t
    return v_i + a_ipoh*dt


def x_full_step(x_ipoh, v_ip1, a_ipoh, dt):
    # x_3/2 = x_1/2 + v_i+1 Delta_t
    return x_ipoh + v_ip1*dt

#--------------------------------------#
# calculate the solar system over time #
#--------------------------------------#


def EvolveSolarSystem(p, n_planets, t_max, screen):
    # number of spatial dimensions
    ndim = 2
    # define the first timestep
    dt = 0.5/365.25
    # define the starting time
    t = 0.0
    # define timestep
    istep = 0
    # save our initial conditions
    for planet in p:
        pygame.draw.circle(screen, planet.get_color(), (planet.x[0], planet.x[1]), planet.get_radius())
    pygame.display.flip()
    # SaveSolarSystem(p, n_planets, t, dt, istep, ndim) TEST TEST TEST TEST
    # begin a loop over the global timescale
    while(t < t_max):
        # check to see if the next step exceeds t_max
        # if so, take a smaller step
        if(t+dt > t_max):
            dt = t_max - t  # limit the step to align with t_max
        # evolve each planet
        for i in range(n_planets):
            while(p[i].t < t+dt):
                # take the first step according to a verlet scheme
                if(p[i].istep == 0):
                    # take the first step
                    for k in range(ndim):
                        p[i].x[k] = x_first_step(
                            p[i].x[k], p[i].v[k], p[i].a_g[k], p[i].dt)
                    # update the acceleration
                    p[i].a_g = SolarGravitationalAcceleration(
                        p[i], solar_system)
                    # update the time by 1/2dt
                    p[i].t += 0.5*p[i].dt
                    # update the timestep
                    p[i].dt = calc_dt(p[i])
                # continue with a normal step
                # limit the planet’s timestep to align with the global step
                if(p[i].t + p[i].dt > t+dt):
                    p[i].dt = t + dt - p[i].t
                # evolve the velocity
                for k in range(ndim):
                    p[i].v[k] = v_full_step(
                        p[i].v[k], p[i].a_g[k], p[i].a_g[k], p[i].dt)
                # evolve the position
                for k in range(ndim):
                    p[i].x[k] = x_full_step(
                        p[i].x[k], p[i].v[k], p[i].a_g[k], p[i].dt)
                # update the acceleration
                p[i].a_g = SolarGravitationalAcceleration(p[i], solar_system)
                # update the time
                p[i].t += p[i].dt
                # compute the new timestep
                p[i].dt = calc_dt(p[i])
                # update the integer timestep
                p[i].istep += 1
        # update the global system time
        t += dt
        # update the global timestep number
        istep += 1
        # output the current state
        for planet in p:
            pygame.draw.circle(screen, planet.get_color(), (planet.x[0], planet.x[1]), planet.get_radius())
        pygame.display.flip()
        # SaveSolarSystem(p, n_planets, t, dt, istep, ndim) TEST TEST TEST TEST
    # print the final steps and time
    print("Time t = ", t)
    print("Maximum t = ", t_max)
    print("Number of steps = ", istep)
    # end
