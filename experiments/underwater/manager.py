import asyncio
import logging 
import sys 
import os
from pyrevolve import parser 
from pyrevolve.custom_logging import logger
from pyrevolve.tol.manage import World 
from pyrevolve.util.supervisor.supervisor_multi import DynamicSimSupervisor
from pyrevolve.revolve_bot import RevolveBot 
from pyrevolve.evolution import fitness 
from pyrevolve.SDF.math import Vector3
from pyrevolve.tol.manage import measures

async def run(): 
    """ The main coroutine, which is started below """ 
    log = logger.create_logger('experiment', handlers=[ logging.StreamHandler(sys.stdout), ])
    # Set debug level to DEBUG
    log.setLevel(logging.DEBUG)

    # Parse command line / file input arguments
    settings = parser.parse_args()

    # Start Simulator
    if settings.simulator_cmd != 'debug':
        simulator_supervisor = DynamicSimSupervisor(
            world_file=settings.world,
            simulator_cmd=settings.simulator_cmd,
            simulator_args=["--verbose"],
            plugins_dir_path=os.path.join('.', 'build', 'lib'),
            models_dir_path=os.path.join('.', 'models'),
            simulator_name='gazebo'
        )
    await simulator_supervisor.launch_simulator(port=settings.port_start)
    await asyncio.sleep(0.1)

    # Connect to the simulator and pause
    connection = await World.create(settings, world_address=('127.0.0.1', settings.port_start))
    await asyncio.sleep(1)

    # initialization finished

    # load robot file
    robot = RevolveBot(_id=settings.test_robot)
    robot.load_file("experiments/examples/yaml/spider.yaml", conf_type='yaml')
    robot.save_file(f'{"experiments/examples/yaml/spider.yaml"}.sdf', conf_type='sdf', add_buoyancy=True)

    # insert robot into the simulator
    robot_manager = await connection.insert_robot(robot, Vector3(0, 0, 0.25), life_timeout=None, add_buoyancy=True)
    await asyncio.sleep(1.0)

    # measures.velocity is not a good way to measure vertical velocity (probably only does horizontal)

    with open('experiments/underwater/water_speed.txt', 'w') as file:
        # Start the main life loop
        i = 0
        while True:
            if i >= 500: break
            #dist = robot_manager._positions[-1][2]
            #print(f" ITER: {i}\n"
                #f" DIST: {dist}")
            #file.write(str(dist)+ '\n')
            await asyncio.sleep(0.1)
            i+=1
    
    file.close()
