from matplotlib import pyplot as plt
from storage import Storage
storage = Storage(path=".")

## Часть 1 
from basic_analysis.exp import ExpDistributionDTO
from view import MainMenu, SaveOrderFlowsMenu, DistributionSelectorMenu

print("Выберите данные из хранилища для входного потока:")
input_orders_params = DistributionSelectorMenu().display_selector()
MainMenu(input_orders_params, storage)

print("Выберите данные из хранилища для случайных величин времени обслуживания:")
serving_duration_params = DistributionSelectorMenu().display_selector()
MainMenu(serving_duration_params, storage)

## serving
from orders import ServicingSystem

serv_system = ServicingSystem(orders_params = input_orders_params, 
                servicing_duration_params = serving_duration_params)
serv_system.service()

## Часть 2-3
SaveOrderFlowsMenu (input_flow_params=input_orders_params, storage = storage, 
                    served_flow = serv_system.serviced_flow, 
                    unserved_flow= serv_system.unserviced_flow).display()

## Часть 4
print(f"П1 m1 = {serv_system.serviced_flow.intervals_len} N = {len(input_orders_params.y)}")
print(f"П2 m2 = {serv_system.unserviced_flow.intervals_len} N = {len(input_orders_params.y)}")

fig = plt.figure(figsize=(12, 8))
fig.suptitle('Длины интервалов между соседними заявками потоков 1 и 2 соответственно')
fig.add_subplot(2,2,2)
plt.hist(serv_system.serviced_flow.intervals, density="true", 
         range=(0,max(serv_system.serviced_flow.intervals)), 
         label=('длины интервалов'))

fig.add_subplot(2,2,1)
plt.hist(serv_system.unserviced_flow.intervals, density="true", 
         range=(0,max(serv_system.unserviced_flow.intervals)), 
         label=('длины интервалов'))
plt.show()