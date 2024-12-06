from plot import GraphVisualizer
import networkx as nx
from networkx.algorithms.approximation import traveling_salesman_problem

# Todos centros de distribuição, caminhões e cidades
import data as dt

from helpers import calcular_distancia
from helpers import rotate_array_until_string
from datetime import datetime
import random

def main():

    initial_timestamp = int(datetime.utcnow().timestamp() * 1000)

    print(dt.centros_distribuicao)
    
    graph_viz = GraphVisualizer()

    for cidade in dt.cidades_brasil:
        if dt.centros_distribuicao['Centro_ID'].str.contains(cidade['cidade'], case=False).any():
            graph_viz.add_node(cidade['cidade'], coordenadas=cidade['coordenadas'], warehouse=True)
        else:
            graph_viz.add_node(cidade['cidade'], coordenadas=cidade['coordenadas'], warehouse=False)

    for i in range(len(dt.cidades_brasil)):
        for j in range(i + 1, len(dt.cidades_brasil)):
            city1 = dt.cidades_brasil[i]['cidade']
            coord1 = dt.cidades_brasil[i]['coordenadas']
            city2 = dt.cidades_brasil[j]['cidade']
            coord2 = dt.cidades_brasil[j]['coordenadas']
            graph_viz.add_edge(city1, city2, weight=calcular_distancia(coord1, coord2))
    
    
    q_entregas = 4000
    prazos_dias_max = 30
    entregas = []

    for i in range(0, q_entregas):
        idx_cidade = random.randint(4, len(dt.cidades_brasil) -1) 
        prazo = int(datetime.utcnow().timestamp() * 1000) + random.randint(0, 86400000 * prazos_dias_max) # due date is now + X days

        c = dt.cidades_brasil[idx_cidade]

        closest_wh = ""
        dist_wh = 100000

        for centro in dt.centros_distribuicao['Centro_ID']:
            for ci in dt.cidades_brasil:
                if centro is ci["cidade"]:
                    dist = calcular_distancia(c["coordenadas"], ci["coordenadas"])
                    if dist < dist_wh:
                        dist_wh = dist
                        closest_wh = ci["cidade"]
                    

        entregas.append({   
                            'cidade': c["cidade"], 
                            'coordenadas': c["coordenadas"], 
                            'prazo': prazo, 
                            'warehouse': closest_wh, 
                            'carga': random.randint(100,300) 
                        })
    entregas_por_prazo = sorted(entregas, key=lambda x: x['cidade'])
    #print(entregas_por_prazo)


    for warehouse in dt.centros_distribuicao['Centro_ID']:
        for truck in range(0, len(dt.caminhoes)):
            #print(f"Truck {truck} from {warehouse}:")
            if dt.caminhoes.iloc[truck]['Centro_Distribuicao'] == warehouse:

                print(f"Truck {truck} from {warehouse}:")

                # Para apenas um caminhão
                total_route_weight = 0
                truck_max_service_kms = dt.caminhoes.iloc[truck]['Distancia_Servico']
                truck_max_load = dt.caminhoes.iloc[truck]['Capacidade_Ton'] * 1000
                truck_cur_load = 0
                max_due_days = 7
                max_due_date = int(datetime.utcnow().timestamp() * 1000) + random.randint(0, 86400000 * max_due_days)

                
                for entrega in entregas_por_prazo[:]:
                    if entrega["warehouse"] == warehouse and int(entrega["prazo"]) <= max_due_date:
                        if truck_cur_load + entrega['carga'] <= truck_max_load:
                            
                            dt.caminhoes.at[truck, 'Items_Carregados'].append(entrega)
                            # remove entrega da lista
                            entregas_por_prazo.remove(entrega)
                            truck_cur_load += entrega['carga']

                print(f"Loaded: {truck_cur_load} out of {truck_max_load}")

                route_calculation_tries = 0 
                tsp_path = []
                while route_calculation_tries <= 5 and (total_route_weight == 0 or total_route_weight > truck_max_service_kms): 
                    
                    if route_calculation_tries > 0:
                        total_route_weight = 0
                        last_item = dt.caminhoes.iloc[truck]['Items_Carregados'][-1]
                        # print(last_item['cidade'])
                        
                        items_to_remove = [entrega for entrega in dt.caminhoes.iloc[truck]['Items_Carregados'] if entrega['cidade'] == last_item['cidade']]
                        for entrega in items_to_remove:
                            dt.caminhoes.iloc[truck]['Items_Carregados'].remove(entrega)
                            entregas_por_prazo.append(entrega)

                        # Reorderna a lista
                        entregas_por_prazo = sorted(entregas_por_prazo, key=lambda x: x['cidade'])

                    
                    cities_list = [warehouse]
                    for entrega in dt.caminhoes.iloc[truck]['Items_Carregados']:
                        if entrega['cidade'] not in cities_list:
                            cities_list.append(entrega['cidade'])

                    # Aplica o TSP na lista de cidades
                    if len(cities_list) > 1:
                        subgraph = graph_viz.G.subgraph(cities_list)
                        tsp_path = traveling_salesman_problem(subgraph, cycle=False)
                       
                        
                        tsp_path = rotate_array_until_string(tsp_path, warehouse)
                        tsp_path.append(warehouse)
                    
                        
                        for i in range(len(tsp_path) - 1):
                            u, v = tsp_path[i], tsp_path[i + 1]
                            
                            total_route_weight += subgraph[u][v]['weight']
                        # print(f"Total weight of the TSP path: {total_route_weight}")                        
                    else: 
                        print("NO DESTINATIONS!!!")
                        break

                    route_calculation_tries += 1 
                
                if len(tsp_path) > 1:
                    print(f"Route: {str(tsp_path)}")  
                    print(f"Total weight of the TSP path: {total_route_weight}")

    
    print(f"ENTREGAS RESTANTES: {len(entregas_por_prazo)}")
    
    
    final_timestamp = int(datetime.utcnow().timestamp() * 1000)

    print(f"Total elapsed time: {final_timestamp - initial_timestamp} ms")

    
    graph_viz.display()       


if __name__ == "__main__":
    main()