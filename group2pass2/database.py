
branches = {
    1: {"rank":"1","name":"Mon's Team","WLT":"24-12-0", "GB":"-"},
    2: {"rank":"2","name":"Bati's Team", "WLT":"22-13-1", "GB":"1.5"},
    3: {"rank":"3","name":"California's Team", "WLT":"21-15-0", "GB":"3"},
    4: {"rank":"4","name":"Kobi's Team","WLT":"20-16-0", "GB":"4"},
    5: {"rank":"5","name":"Big Baller Brand's Team", "WLT":"19-17-0", "GB":"4.5"},
}
def get_standing(rank):
    return standings[rank]

def get_standings():
    standings_list = []

    for i,v in standings.items():
        standing = v
        standing.setdefault("rank",i)
        standings_list.append(standings)

    return standings_list

def get_branch(code):
    return branches[code]

def get_branches():
    branch_list = []

    for i,v in branches.items():
        branch = v
        branch.setdefault("code",i)
        branch_list.append(branch)

    return branch_list