# -*- coding: utf-8 -*-
from itertools import permutations
"""
initialize
"""
inf = 9999
min_battery_to_return = 30


"""
class 
"""   

class MobileAgents:
    def __init__(self, name):
        self.name = name
        self.path = []
        self.location = charginglist[0]
        self.battery = 100
        self.on_the_way_of_charging = 0
    
    def update_location(self,location):
        self.location = location
        
    def update_battery(self,battery):
        self.battery = battery
        
    def add_path(self, vertex):
        self.path.append(vertex)
        
    def clear_path(self):
        self.path.clear()
    
    def go_to_charge(self):
        self.on_the_way_of_charging = 1
        
    def finish_charge(self):
        self.on_the_way_of_charging = 0

"""
function
"""  

def dijkstra_algorithm_with_path(start: int) -> list:
    passed = [start]
    nopass = [x for x in range(len(maps)) if x != start]
    #initialize dis
    dis = [inf for x in range(len(maps))]
    dis [start] = 0
    if start-row >= 0:
        dis[start-row] = maps[start][0]
    if start+row < row*col:
        dis[start+row] = maps[start][1]
    if start-1 >= 0:
        dis[start-1] = maps[start][2]
    if start+1 < col*row:
        dis[start+1] = maps[start][3]
    path = [-1 for i in range(len(maps))]
    while len(nopass):
        idx = nopass[0]
        for i in nopass:
            if dis[i] < dis[idx]: idx = i

        nopass.remove(idx)
        passed.append(idx)
        
        for i in nopass:
            if i == idx-row:
                if dis[idx] + maps[idx][0] < dis[i]: 
                    dis[i] = dis[idx] + maps[idx][0]
                    path[i] = idx
            elif i == idx+row:
                if dis[idx] + maps[idx][1] < dis[i]: 
                    dis[i] = dis[idx] + maps[idx][1]
                    path[i] = idx
            elif i == idx-1:
                if dis[idx] + maps[idx][2] < dis[i]: 
                    dis[i] = dis[idx] + maps[idx][2]
                    path[i] = idx
            elif i == idx+1:
                if dis[idx] + maps[idx][3] < dis[i]: 
                    dis[i] = dis[idx] + maps[idx][3]
                    path[i] = idx
    return path

def dijkstra_algorithm_without_path(start: int) -> list:
    passed = [start]
    nopass = [x for x in range(len(maps)) if x != start]
    #initialize dis
    dis = [inf for x in range(len(maps))]
    dis [start] = 0
    if start-row >= 0:
        dis[start-row] = maps[start][0]
    if start+row < row*col:
        dis[start+row] = maps[start][1]
    if start-1 >= 0:
        dis[start-1] = maps[start][2]
    if start+1 < col*row:
        dis[start+1] = maps[start][3]
    
    while len(nopass):
        idx = nopass[0]
        for i in nopass:
            if dis[i] < dis[idx]: idx = i

        nopass.remove(idx)
        passed.append(idx)

        for i in nopass:
            if i == idx-row:
                if dis[idx] + maps[idx][0] < dis[i]: 
                    dis[i] = dis[idx] + maps[idx][0]
            elif i == idx+row:
                if dis[idx] + maps[idx][1] < dis[i]: 
                    dis[i] = dis[idx] + maps[idx][1]
            elif i == idx-1:
                if dis[idx] + maps[idx][2] < dis[i]: 
                    dis[i] = dis[idx] + maps[idx][2]
            elif i == idx+1:
                if dis[idx] + maps[idx][3] < dis[i]: 
                    dis[i] = dis[idx] + maps[idx][3]
    return dis

def store_path(start: int,end: int) -> list:
    path = dijkstra_algorithm_with_path(start)
    result = []
    loc = end
    result.insert(0,end)
    while path[loc]!= -1:
        result.insert(0,path[loc])
        loc = path[loc]
    return result

def tsp_with_path(start:int):
    total_list = tasklist
    total_list.insert(0,start)
    distance = [[0 for x in range(len(total_list))] for y in range(len(total_list))]
    for i in range(len(total_list)):
        temp = dijkstra_algorithm_without_path(total_list[i])
        for j in range(len(total_list)):
            distance[i][j] = temp[total_list[j]]
    min_path = inf
    order_list = [y for y in range(len(total_list))]
    next_permutation = permutations(order_list)
    for i in next_permutation:
        current_pathweight = 0
        k = 0
        for j in i:
            current_pathweight = current_pathweight + distance[k][j]
            k = j
        if (min_path > current_pathweight):
            min_path = current_pathweight
            path = []
            for j in i:
                path.append(total_list[j])
    path1 = []
    for i in range(len(path)-1):
        temp = store_path(path[i], path[i+1])
        for j in temp:
            path1.append(j)
    del tasklist[0]
    return path1


def find_nearest_charging_station(start:int) ->list:
    dis = dijkstra_algorithm_without_path(start)
    path = dijkstra_algorithm_with_path(start)
    temp_index = charginglist[0]
    temp_value = dis[charginglist[0]]
    for x in charginglist:
        if dis[x] < temp_value:
            temp_index = x
            temp_value = dis[x]
    print("go to charger at index",temp_index)
    result = []
    end = temp_index
    loc = end
    result.insert(0,end)
    while path[loc]!= -1:
        result.insert(0,path[loc])
        loc = path[loc]
    return result
        

"""
main
"""

if __name__ == "__main__":
    #initialization
    """only for administrators
    method = 0
    row = 10
    col = 10
    tasklist = [3,6,8,14,47,51,66,81]
    obstaclelist = [4,13,17,24,42,43,52,53,55,65,75,72,73,78,79,82]
    charginglist = [0,99]
    time = 1000
    cost_of_moving = 2
    """
    method = input("Enter 0 if you want to complete the tasks in order, enter 1 to traverse in a shortest cost:")
    while method != '1' and method != '0':
        method = input("invalid input! Please try again and enter either 0 or 1:")
    method = int(method)
    row = input("please enter the row of your map:")
    while row.isdigit() == False:
        row = input("invalid input! Please try again:")
    row = int(row)
    
    col = input("please enter the column of your map:")
    while col.isdigit() == False:
        col = input("invalid input! Please try again:")
    col = int(col)
    #initialize_tasklist[]
    tasklist = []
    task = input("please enter the index of task:")
    while task != 'finish' or tasklist ==[]:
        if task.isdigit():
            task = int(task)
            if task >= 0 and task < row*col:
                if task in tasklist:
                    print("task already exists, please try again")
                else:
                    tasklist.append(task)
            else:
                print("task out of range[ 0,", row*col-1,"], please try again")
        elif task == 'finish':
            print("no index in tasklist, please enter at least one valid index")
        else:
            print("invalid task, please try again and enter an integer")
        task = input("please enter the index of task or 'finish':")
    #initialize_obstacle[]
    obstaclelist = []
    obstacle = input("please enter the index of obstacle:")
    while obstacle != 'finish':
        if obstacle.isdigit():
            obstacle = int(obstacle)
            if obstacle >= 0 and obstacle < row*col:
                if obstacle in obstaclelist:
                    print("obstacle already exists, please try again")
                elif obstacle in tasklist:
                    print("this location already exists a task, please try again")
                else:
                    obstaclelist.append(task)
            else:
                print("obstacle out of range[ 0,", row*col-1,"], please try again")
        else:
            print("invalid obstacle, please try again and enter an integer")
        obstacle = input("please enter the index of obstacle or 'finish':")
    #initialize_charginglist[]
    charginglist = []
    charging = input("please enter the index of charging station, the first charging station will be the starting point:")
    while charging != 'finish' or charginglist ==[]:
        if charging.isdigit():
            charging = int(charging)
            if charging >= 0 and charging < row*col:
                if charging in tasklist:
                    print("charging_station already exists, please try again")
                elif charging in tasklist:
                    print("this location already exists a task, please try again")
                elif charging in obstaclelist:
                    print("this location already exists an obstacle, please try again")
                else:
                    charginglist.append(charging)
            else:
                print("charging_station out of range[ 0,", row*col-1,"], please try again")
        elif charging == 'finish':
            print("no index in charginglist, please enter at least one valid index")
        else:
            print("invalid charging_station, please try again and enter an integer")
        charging = input("please enter the index of charging_station or 'finish':")
    #initalize_time
    time = input("please enter the maximum operating time(recommend > 300):")
    while time.isdigit() == False:
        row = input("invalid input! Please try again:")
    time = int(time)
    #initialize_cost_of_moving
    cost_of_moving = input("please enter the moving cost of power for each step:")
    while cost_of_moving.isdigit() == False:
        cost_of_moving = input("invalid input! Please try again:")
    cost_of_moving = int(row)
    cost = 4
    task_finished = 0
    #initialize_map
    maps = [[cost for x in range(4)] for y in range(row*col)]
    for i in range(0,row*col):
        #check if on the edge
        if i % row == 0: #left
            maps[i][2] = inf 
        if i % row == row-1: #right
            maps[i][3] = inf
        if i < row:#up
            maps[i][0] = inf
        if i > (row*(col-1)-1) and i < row*col: #down
            maps[i][1] = inf
        #check if in the obstaclelist
        if i in obstaclelist:
            for j in range(4):
                maps[i][j] = inf
            if i-row >= 0 :
                maps[i-row][1] = inf
            if i+row < row*col:
                maps[i+row][0] = inf
            if (i-1) % row != row-1:
                maps[i-1][3] = inf
            if (i+1) % row != 0:
                maps[i+1][2] = inf
    if method == 0:
        agent = MobileAgents('a')
        new_path = store_path(agent.location, tasklist[0])
        for x in new_path:
            agent.add_path(x)
    else:
        agent = MobileAgents('a') 
        new_path = tsp_with_path(agent.location)
        for x in new_path:
            agent.add_path(x)
    #end_initialization
    while time>0 and agent.battery>0:
        if method == 0:#dijkstra algorithm
            if agent.location in charginglist and agent.battery < 100: #reach the charging station and battery <100
                time = time - 5
                agent.battery = 100
                agent.clear_path()
                agent.finish_charge()
                new_path = store_path(agent.location, tasklist[0])
                for x in new_path:
                    agent.add_path(x)
            elif agent.location in tasklist: #reach the task
                print("finish task at vertex",agent.location)
                tasklist.remove(agent.location)
                if tasklist == []:
                    print("all the tasks have been finished")
                    break
                else:
                    agent.clear_path()
                    new_path = store_path(agent.location, tasklist[0])
                    for x in new_path:
                        agent.add_path(x)
            if agent.battery < min_battery_to_return and agent.on_the_way_of_charging == 0:
                agent.go_to_charge()
                agent.clear_path()
                new_path = find_nearest_charging_station(agent.location)
                for x in new_path:
                    agent.add_path(x)
            
            if agent.path[0] == agent.location-row:
                time = time - maps[agent.location][0]
            elif agent.path[0] == agent.location+row:
                time = time - maps[agent.location][1]
            elif agent.path[0] == agent.location-1:
                time = time - maps[agent.location][2]
            elif agent.path[0] == agent.location+1:
                time = time - maps[agent.location][3]
            agent.location = agent.path[0]
            agent.battery = agent.battery - cost_of_moving#deduct battery
            del agent.path[0]
        else:#tsp
            if agent.location in charginglist and agent.battery < 100:
                time = time - 5
                agent.battery = 100
                agent.clear_path()
                agent.finish_charge()
                new_path = tsp_with_path(agent.location)
                for x in new_path:
                    agent.add_path(x)
            elif agent.location in tasklist: 
                print("finish task at vertex",agent.location)
                tasklist.remove(agent.location)
                if tasklist == []:
                    print("all the tasks have been finished")
                    break
            if agent.battery < min_battery_to_return and agent.on_the_way_of_charging == 0:#battery< min_battery_to_return
                agent.go_to_charge()
                agent.clear_path()
                new_path = find_nearest_charging_station(agent.location)
                for x in new_path:
                    agent.add_path(x)
            #deduct time
            if agent.path[0] == agent.location-row:
                time = time - maps[agent.location][0]
            elif agent.path[0] == agent.location+row:
                time = time - maps[agent.location][1]
            elif agent.path[0] == agent.location-1:
                time = time - maps[agent.location][2]
            elif agent.path[0] == agent.location+1:
                time = time - maps[agent.location][3]
            agent.location = agent.path[0]
            agent.battery = agent.battery - cost_of_moving#deduct power
            del agent.path[0]
            
    print ("remain battery",agent.battery)
    print ("remain time",time)
  
    