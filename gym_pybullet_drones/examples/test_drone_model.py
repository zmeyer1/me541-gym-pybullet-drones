from gym_pybullet_drones.utils.enums import DroneModel

print("ALL DroneModel ENUM MEMBERS:")
for model in DroneModel:
    print(f"{model.name} = {model.value}")
