import random

# 課程資料
courses = [
    {'teacher': '甲', 'name': '機率', 'hours': 2},
    {'teacher': '甲', 'name': '線代', 'hours': 3},
    {'teacher': '甲', 'name': '離散', 'hours': 3},
    {'teacher': '乙', 'name': '視窗', 'hours': 3},
    {'teacher': '乙', 'name': '科學', 'hours': 3},
    {'teacher': '乙', 'name': '系統', 'hours': 3},
    {'teacher': '乙', 'name': '計概', 'hours': 3},
    {'teacher': '丙', 'name': '軟工', 'hours': 3},
    {'teacher': '丙', 'name': '行動', 'hours': 3},
    {'teacher': '丙', 'name': '網路', 'hours': 3},
    {'teacher': '丁', 'name': '媒體', 'hours': 3},
    {'teacher': '丁', 'name': '工數', 'hours': 3},
    {'teacher': '丁', 'name': '動畫', 'hours': 3},
    {'teacher': '丁', 'name': '電子', 'hours': 4},
    {'teacher': '丁', 'name': '嵌入', 'hours': 3},
    {'teacher': '戊', 'name': '網站', 'hours': 3},
    {'teacher': '戊', 'name': '網頁', 'hours': 3},
    {'teacher': '戊', 'name': '演算', 'hours': 3},
    {'teacher': '戊', 'name': '結構', 'hours': 3},
    {'teacher': '戊', 'name': '智慧', 'hours': 3}
]

teachers = ['甲', '乙', '丙', '丁', '戊']

rooms = ['A', 'B']

slots = [
    'A11', 'A12', 'A13', 'A14', 'A15', 'A16', 'A17',
    'A21', 'A22', 'A23', 'A24', 'A25', 'A26', 'A27',
    'A31', 'A32', 'A33', 'A34', 'A35', 'A36', 'A37',
    'A41', 'A42', 'A43', 'A44', 'A45', 'A46', 'A47',
    'A51', 'A52', 'A53', 'A54', 'A55', 'A56', 'A57',
    'B11', 'B12', 'B13', 'B14', 'B15', 'B16', 'B17',
    'B21', 'B22', 'B23', 'B24', 'B25', 'B26', 'B27',
    'B31', 'B32', 'B33', 'B34', 'B35', 'B36', 'B37',
    'B41', 'B42', 'B43', 'B44', 'B45', 'B46', 'B47',
    'B51', 'B52', 'B53', 'B54', 'B55', 'B56', 'B57',
]

# 初始化變數
current_schedule = {slot: None for slot in slots}

def calculate_conflicts(schedule):
    """計算排課表中的衝突數"""
    conflicts = 0
    teacher_slots = {teacher: [] for teacher in teachers}
    
    for slot, course in schedule.items():
        if course:
            teacher = course['teacher']
            teacher_slots[teacher].append(slot)
    
    for teacher, slots in teacher_slots.items():
        if len(slots) > len(set(slots)):
            conflicts += len(slots) - len(set(slots))
    
    return conflicts

def get_neighbor(schedule):
    """生成鄰居排課表"""
    new_schedule = schedule.copy()
    slot1, slot2 = random.sample(slots, 2)
    new_schedule[slot1], new_schedule[slot2] = new_schedule[slot2], new_schedule[slot1]
    return new_schedule

# 初始解
for course in courses:
    hours_needed = course['hours']
    allocated_hours = 0
    
    for slot in slots:
        if current_schedule[slot] is None:
            current_schedule[slot] = course
            allocated_hours += 1
            if allocated_hours == hours_needed:
                break

# 爬山演算法
current_conflicts = calculate_conflicts(current_schedule)
iterations = 10000

for _ in range(iterations):
    neighbor_schedule = get_neighbor(current_schedule)
    neighbor_conflicts = calculate_conflicts(neighbor_schedule)
    
    if neighbor_conflicts < current_conflicts:
        current_schedule = neighbor_schedule
        current_conflicts = neighbor_conflicts
    
    if current_conflicts == 0:
        break

# 輸出結果
for slot, course in current_schedule.items():
    if course:
        print(f"{slot}: {course['teacher']} - {course['name']}")
    else:
        print(f"{slot}: 空堂")
