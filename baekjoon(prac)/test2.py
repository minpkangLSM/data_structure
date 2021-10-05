
def solution(n, a, cards):
    count = 0
    card_len = len(cards)
    j_list = []
    win_dict = {"P" : "S", "R" : "P", "S" : "R"}
    if card_len == a :
        cards = cards + "A"
    elif a==0:
        cards = "A"+cards
    elif card_len > a:
        cards = cards[:a] + "A" + cards[a:]

    while len(cards)>1:

        league = []
        for i in range(0, len(cards), 2) :
            temp = list(cards[i:i+2])
            temp_len = len(temp)
            if temp_len == 2:
                if "A" in temp :
                    temp.remove("A")
                    rest = temp[0]
                    if len(j_list)==0:
                        j_list.append(win_dict[rest])
                    else :
                        j = j_list[-1]
                        if j=="P" and rest=="S":
                            j_list.append("R")
                            count+=1
                        elif ord(j) >= ord(rest):
                            j_list.append(win_dict[rest])
                            count+=1
                    league.append("A")
                else :
                    if "P" in temp and "S" in temp:
                        league.append("S")
                        continue
                    front = ord(temp[0])
                    rear = ord(temp[1])
                    if front == rear : continue
                    min_v = min(front, rear)
                    league.append(chr(min_v))
            else :
                league.append(temp[0])
        cards = league

    return count

if __name__ == "__main__":
    n = 3
    a = 2
    cards = "RP"
    count = solution(n, a, cards)
    print(count)