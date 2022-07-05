from orders.flows import OrdersFlow

class ServicingSystem:

    def __init__(self, orders_params, servicing_duration_params) -> None:
        self.orders_params = orders_params
        self.servicing_duration_params = servicing_duration_params   

    def service(self):
        self.serviced_flow = OrdersFlow([])
        self.unserviced_flow = OrdersFlow([])                

        # входной поток
        latest_order = 0
        for index, tau in enumerate(self.orders_params.y):
            #интервал между заявками
            latest_order += tau
            
            # если заявку невозможно обслужить
            if latest_order <= (self.serviced_flow.tau[-1] if len(self.serviced_flow.tau)>0 else 0):
                self.unserviced_flow.tau.append(latest_order)
            else:
                # для i-й обслуженной заявки i-е время обслуживание из сгенерированного списка
                servicing_duration = self.servicing_duration_params.y[len(self.serviced_flow.tau)]
                # заявка обслужена
                self.serviced_flow.tau.append(latest_order + servicing_duration)
