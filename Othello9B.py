import sys
CACHEDSOLUTION={}
MOVES={}
XBOARDS={}
OBOARDS={}
CACHEDBOARDSTATS={}
def findPossibleMoves(token, BOARD):
    possibleMoves={} #moves dictionary
    copyBoard=[*BOARD]
    if token.lower()=='x':
        otherToken='o'
    else: otherToken='x'
    for idx, val in enumerate(BOARD):
        if val=='.':
            #check up
            if idx-8>=0 and BOARD[idx-8].lower()==otherToken:
                tmpidx = idx
                affected=[tmpidx]
                while tmpidx-8>=0 and BOARD[tmpidx-8].lower()==otherToken:
                    tmpidx-=8
                    affected.append(tmpidx)
                if tmpidx-8>=0 and BOARD[tmpidx-8]==token:
                    #affected.append(tmpidx-8)
                    #opyBoard[tmpidx-8]='*'
                    copyBoard[idx]='*'
                    possibleMoves[idx]=affected
            #check down
            if idx+8<len(BOARD) and BOARD[idx+8].lower()==otherToken:
                tmpidx=idx
                affected=[tmpidx]
                while tmpidx+8<len(BOARD) and BOARD[tmpidx+8].lower()==otherToken:
                    tmpidx+=8
                    affected.append(tmpidx)
                if tmpidx+8<len(BOARD) and BOARD[tmpidx+8]==token:
                    #affected.append(tmpidx+8)
                    #copyBoard[tmpidx+8]='*'
                    copyBoard[idx] = '*'
                    if idx in possibleMoves: possibleMoves[idx]+=affected
                    else:possibleMoves[idx]=affected
            #check right
            if (idx%8)+1<8 and BOARD[idx+1].lower()==otherToken:
                tmpidx=idx
                affected=[tmpidx]
                while(tmpidx%8)+1<8 and BOARD[tmpidx+1].lower()==otherToken:
                    tmpidx+=1
                    affected.append(tmpidx)
                if (tmpidx%8)+1<8 and BOARD[tmpidx+1]==token:
                    #affected.append(tmpidx+1)
                    #copyBoard[tmpidx+1]='*'
                    copyBoard[idx] = '*'
                    if idx in possibleMoves: possibleMoves[idx]+=affected
                    else:possibleMoves[idx]=affected
            #check left
            if (idx%8)-1>=0 and BOARD[idx-1].lower()==otherToken:
                tmpidx=idx
                affected=[tmpidx]
                while(tmpidx%8)-1>=0 and BOARD[tmpidx-1].lower()==otherToken:
                    tmpidx-=1
                    affected.append(tmpidx)
                if (tmpidx%8)-1>=0 and BOARD[tmpidx-1]==token:
                    #affected.append(tmpidx-1)
                    #copyBoard[tmpidx-1]='*'
                    copyBoard[idx] = '*'
                    if idx in possibleMoves: possibleMoves[idx]+=affected
                    else:possibleMoves[idx]=affected
            #check diag down left
            if (idx%8)-1>=0 and idx+7<len(BOARD) and BOARD[idx+7].lower()==otherToken:
                tmpidx=idx
                affected = [tmpidx]
                while(tmpidx%8)-1>=0 and tmpidx+7<len(BOARD) and BOARD[tmpidx+7].lower()==otherToken:
                    tmpidx+=7
                    affected.append(tmpidx)
                if (tmpidx%8)-1>=0 and tmpidx+7<len(BOARD) and BOARD[tmpidx+7]==token:
                    #affected.append(tmpidx+7)
                    #copyBoard[tmpidx+7]='*'
                    copyBoard[idx] = '*'
                    if idx in possibleMoves: possibleMoves[idx]+=affected
                    else:possibleMoves[idx]=affected
            #check diag up left
            if (idx%8)-1>=0 and idx-9>=0 and BOARD[idx-9].lower()==otherToken:
                tmpidx=idx
                affected = [tmpidx]
                while(tmpidx%8)-1>=0 and tmpidx-9>=0 and BOARD[tmpidx-9].lower()==otherToken:
                    tmpidx-=9
                    affected.append(tmpidx)
                if (tmpidx%8)-1>=0 and tmpidx-9>=0 and BOARD[tmpidx-9]==token:
                    #affected.append(tmpidx-9)
                    #copyBoard[tmpidx-9]='*'
                    copyBoard[idx] = '*'
                    if idx in possibleMoves: possibleMoves[idx]+=affected
                    else:possibleMoves[idx]=affected
            #check diag down right
            if(idx%8)+1<8 and idx+9<len(BOARD) and BOARD[idx+9].lower()==otherToken:
                tmpidx=idx
                affected=[tmpidx]
                while (tmpidx%8)+1<8 and tmpidx+9<len(BOARD) and BOARD[tmpidx+9].lower()==otherToken:
                    tmpidx+=9
                    affected.append(tmpidx)
                if (tmpidx%8)+1<8 and tmpidx+9<len(BOARD) and BOARD[tmpidx+9]==token:
                    #affected.append(tmpidx+9)
                    #copyBoard[tmpidx+9]='*'
                    copyBoard[idx] = '*'
                    if idx in possibleMoves: possibleMoves[idx]+=affected
                    else:possibleMoves[idx]=affected
            #check diag up right
            if (idx % 8) + 1 < 8 and idx -7 >=0 and BOARD[idx -7].lower() == otherToken:
                tmpidx = idx
                affected = [tmpidx]
                while (tmpidx % 8) + 1 < 8 and tmpidx -7>=0 and BOARD[tmpidx -7].lower() == otherToken:
                    tmpidx -=7
                    affected.append(tmpidx)
                if (tmpidx % 8) + 1 < 8 and tmpidx -7>=0 and BOARD[tmpidx -7] == token:
                    #affected.append(tmpidx -7)
                    #copyBoard[tmpidx -7] = '*'
                    copyBoard[idx] = '*'
                    if idx in possibleMoves: possibleMoves[idx]+=affected
                    else:possibleMoves[idx]=affected
    newBoard=''.join(copyBoard)
    return newBoard, possibleMoves
def applyMoves(possibleMoves, index, board,token):
    changeBoard=[*board]
    for i in possibleMoves[index]:
        changeBoard[i]=token
    return changeBoard
def display(board):
    for i in range(0, 64, 8):
        print(board[i:i+8])
def alphaBeta(brd, tkn,lower,upper):
    # return list of [guaranteed min score, reversed move sequence]
    #lower is minimum acceptable value, upper is max
    if tkn == 'x':oTkn = 'o'
    else:oTkn = 'x'
    if '.' not in brd:
        score = [(brd.count(tkn) - brd.count(oTkn))]
        return score
    if (brd,tkn) in MOVES:
        allPossibleMoves=MOVES[(brd, tkn)]
    else:
        newB, allPossibleMoves = findPossibleMoves(tkn, brd)
        MOVES[(brd,tkn)]=allPossibleMoves
    if (brd,oTkn) in MOVES: oMoves=MOVES[(brd,oTkn)]
    else:
        onewB, oMoves = findPossibleMoves(oTkn, brd)
        MOVES[(brd,oTkn)]=oMoves
    if len(allPossibleMoves)==0 and len(oMoves)==0:
        score = [(brd.count(tkn) - brd.count(oTkn))]
        return score
    if len(allPossibleMoves)==0:
        tempSol = alphaBeta(brd,oTkn,-upper,-lower)+[-1]
        tempSol[0]*=-1
        return tempSol
    best = [lower-1]
    for mv in allPossibleMoves:
        if tkn=='x' and (brd, mv) in XBOARDS: tmpBoard = XBOARDS[(brd,mv)]
        elif tkn=='o' and (brd, mv) in OBOARDS: tmpBoard = OBOARDS[(brd,mv)]
        else:
            tmpBoard = ''.join(applyMoves(allPossibleMoves, mv, brd,tkn))
            if tkn=='x': XBOARDS[(brd,mv)]=tmpBoard
            else: OBOARDS[(brd,mv)]=tmpBoard
        nm = alphaBeta(tmpBoard,oTkn,-upper,-lower)
        score = -nm[0]
        if score>upper:
            return [score]
        if score<lower:
            continue
        #else we have improvement
        best = [score]+nm[1:]+[mv]
        lower = score+1
    return best
def alphabetaMG(brd, tkn, lower, upper, maxDepth):
  # midgame alpha/beta: returns [minBrdEval, *[reverse move sequence]]
  tB = ''.join(brd)
  if tkn=='x': enemy = 'o'
  else: enemy = 'x'
  if (tB, tkn) in MOVES:
      psblMoves = MOVES[(tB, tkn)]
  else:
    tmpB, psblMoves = findPossibleMoves(tkn, brd)
    MOVES[(tB, tkn)]=psblMoves
  if (tB, enemy) in MOVES: eMoves = MOVES[(tB, enemy)]
  else:
    eB, eMoves = findPossibleMoves(enemy, brd)
    MOVES[(tB, enemy)] = eMoves
  if brd.count('.')==0 or (len(psblMoves)==0 and len(eMoves)==0):
    return [10000000000000000000000000]                  # ie. the real truth (unexpected game over)

  if not maxDepth:                                      # Time for a board evaluation
    if (tB, tkn) in CACHEDBOARDSTATS: tpl = CACHEDBOARDSTATS[(tB, tkn)]
    else:
        tpl = calcBoardStats(brd, tkn, enemy, psblMoves)
        CACHEDBOARDSTATS[(tB, tkn)]=tpl
    statWeights = [10, 801.724, 382.026, 78.922, 74.396, 10]
    # tpl is (TokenCt, mobility, square types, cx danger, stability)   # frontier ct - not used
    brdVal = sum(tpl[i]*statWeights[i] for i in range(len(tpl)))
    return [brdVal]

  if len(psblMoves)==0:
    # else we must pass
    nm = alphabetaMG(brd, enemy, -upper, -lower, maxDepth-1)
    return [-nm[0]] + nm[1:] + [-1]
  # Here comes the recursive part
  best = [1-lower]
  for mv in psblMoves:
    if tkn=='x' and (tB, mv) in XBOARDS: appliedBoard = XBOARDS[(tB, mv)]
    elif tkn=='o' and (tB, mv) in OBOARDS: appliedBoard = OBOARDS[(tB, mv)]
    else:
        appliedBoard = ''.join(applyMoves(psblMoves,mv,brd,tkn))
        if tkn=='x': XBOARDS[(tB, mv)]=appliedBoard
        else: OBOARDS[(tB, mv)]=appliedBoard
    ab = alphabetaMG(appliedBoard,enemy, -upper, -lower, maxDepth-1)
    if -ab[0] > upper: return [-ab[0]]                     # Our move is too good
    if ab[0]<best[0]:                                      # Our move is an improvement
      best = ab + [mv]                                     #   Note the new best
      lower = -best[0]+1                                   #   Note the new lower bound
  return [-best[0]] + best[1:]                             # return the best that we found
def calcBoardStats(brd, tkn, enemy, psblMoves):
    #piece difference, frontier disks, and disk squares
    weights = [20, -3, 11, 8, 8, 11, -3, 20,-3, -7, -4, 1, 1, -4, -7, -3,11, -4, 2, 2, 2, 2, -4, 11,8, 1, 2, -3, -3, 2, 1, 8,8, 1, 2, -3, -3, 2, 1, 8,11, -4, 2, 2, 2, 2, -4, 11,-3, -7, -4, 1, 1, -4, -7, -3,20, -3, 11, 8, 8, 11, -3, 20]
    X1=[-1, -1, 0, 1, 1, 1, 0, -1]
    Y1=[0, 1, 1, 1, 0, -1, -1, -1]
    f=0
    my_tiles = opp_tiles = d = my_front_tiles = opp_front_tiles = 0
    for i,val in enumerate(brd):
        if val==tkn:
            my_tiles+=1
            d+=weights[i]
        if val==enemy:
            opp_tiles+=1
            d-=weights[i]
        if val=='.':
            row = i//8
            col = i%8
            for k in range(8):
                x = row+X1[k]
                y = col+Y1[k]
                if x>=0 and x<8 and y>=0 and y<8 and brd[8*(x) + y]=='.':
                    if brd[(8*row)+col]==tkn:   my_front_tiles+=1
                    else:opp_front_tiles+=1
                    break
    if my_tiles>opp_tiles: p = (100.0 * my_tiles)/(my_tiles + opp_tiles)
    elif my_tiles<opp_tiles: p = -(100.0 * opp_tiles)/(my_tiles + opp_tiles)
    else: p=0
    if my_front_tiles>opp_front_tiles: f = -(100.0 * my_front_tiles)/(my_front_tiles + opp_front_tiles)
    if my_front_tiles<opp_front_tiles: f = (100.0 * opp_front_tiles)/(my_front_tiles + opp_front_tiles)
    else: f=0
    #Corner Occupancy
    myCorners=oppCorners=0
    if brd[0]==tkn: myCorners+=1
    elif brd[0]==enemy: oppCorners+=1
    if brd[7]==tkn: myCorners+=1
    elif brd[7]==enemy: oppCorners+=1
    if brd[56]==tkn: myCorners+=1
    elif brd[56]==enemy: oppCorners+=1
    if brd[63]==tkn: myCorners+=1
    elif brd[63]==enemy: oppCorners+=1
    c=25*(myCorners-oppCorners)
    #corners closeness
    mine = opp = 0
    if brd[0]=='.':
        if brd[1]==tkn: mine+=1
        elif brd[1]==enemy: opp+=1
        if brd[8]==tkn: mine+=1
        elif brd[8]==enemy:opp+=1
        if brd[9]==tkn: mine+=1
        elif brd[9]==enemy: opp+=1
    if brd[7]=='.':
        if brd[6]==tkn: mine+=1
        elif brd[6]==enemy: opp+=1
        if brd[15]==tkn: mine+=1
        elif brd[15]==enemy:opp+=1
        if brd[14]==tkn: mine+=1
        elif brd[14]==enemy: opp+=1
    if brd[56]=='.':
        if brd[48]==tkn: mine+=1
        elif brd[48]==enemy: opp+=1
        if brd[49]==tkn: mine+=1
        elif brd[49]==enemy:opp+=1
        if brd[57]==tkn: mine+=1
        elif brd[57]==enemy: opp+=1
    if brd[63]=='.':
        if brd[62]==tkn: mine+=1
        elif brd[62]==enemy: opp+=1
        if brd[55]==tkn: mine+=1
        elif brd[55]==enemy:opp+=1
        if brd[54]==tkn: mine+=1
        elif brd[54]==enemy: opp+=1
    l = -12.5 * (mine - opp)
    #Mobility
    oB, oPsbls = findPossibleMoves(enemy, brd)
    if len(psblMoves)>len(oPsbls): m = (100.0 * len(psblMoves))/(len(psblMoves) + len(oPsbls))
    elif len(psblMoves)<len(oPsbls): m = -(100.0 * len(oPsbls))/(len(psblMoves) + len(oPsbls))
    else: m = 0
    return [p, c, l, m, f,d]
def showSolution(token, BOARD,mov=-1):
    newB, posMoves = findPossibleMoves(token, BOARD)
    display(newB)
    print()
    placesToGo=set()
    for i in posMoves:
        placesToGo.add(i)
    print("Possible moves for " + token + ': ' + str(placesToGo))
    if token=='x': enemy='o'
    else: enemy='x'
    if BOARD.count('.')<=12:
        sol = alphaBeta(BOARD, tokenToPlay,-len(BOARD),len(BOARD))
        #print('Min score: ' + str(-1*sol[0]) + '; move sequence: ' + str(sol[1:]))
        print('Min score: ' + str(sol[0]) + '; move sequence: ' + str(sol[1:]))
    elif BOARD.count('.')<=50:
        upper = 100000 * len(BOARD)  # Just in case :)
        best = [upper]  # The negative of lower
        for maxDepth in range(1, 7, 1):  # Iterative deepening to level 6
            tmpB,psblMoves = findPossibleMoves(tokenToPlay,BOARD)
            for mv in psblMoves:
                ab = alphabetaMG(applyMoves(psblMoves,mv, BOARD,token),enemy, -upper, best[0], maxDepth - 1)
                if -ab[0] < -best[0]: continue  # ab[0] & best[0] from the enemy's pt of view
                best = ab + [mv]  # A new personal best
                print("At depth {} AB-MG returns {}".format(maxDepth, best))  # An improved move
    else:
        print("My move is: " + str(makeDefaultMove(posMoves, token, BOARD)))
def makeDefaultMove(psblPlaces, tkn, brd):
    if tkn=='x': enemy = 'o'
    else: enemy = 'x'
    corners = {0:[1,8,9],7:[6,14,15],56:[48, 57, 49], 63:[62, 55, 54]}
    weights = [20, -3, 11, 8, 8, 11, -3, 20, -3, -7, -4, 1, 1, -4, -7, -3, 11, -4, 2, 2, 2, 2, -4, 11, 8, 1, 2, -3, -3,
               2, 1, 8, 8, 1, 2, -3, -3, 2, 1, 8, 11, -4, 2, 2, 2, 2, -4, 11, -3, -7, -4, 1, 1, -4, -7, -3, 20, -3, 11,
               8, 8, 11, -3, 20]
    listOfMoves = [i for i in psblPlaces]
    #play to corners if possible, otherwise don't play around corners
    for c in corners:
        if c in listOfMoves:
            return c
        else:
            for j in corners[c]:
                if len(listOfMoves)==1 and j in listOfMoves: return j
                elif j in listOfMoves:
                    listOfMoves.remove(j)
    minNum = 64
    mvToReturn = 64
    #pick the move that minimizes opponent moves
    for mv in listOfMoves:
        temp = findPossibleMoves(enemy, applyMoves(psblPlaces,mv, brd, tkn))
        if len(temp)<minNum:
            minNum = len(temp)
            mvToReturn = mv
    return mvToReturn
def main():
    tokens='XxOo'
    BOARD='.'*27+'OX......XO' + '.'*27
    cells='abcdefgh'
    global tokenToPlay
    tokenToPlay='x'
    global moves
    moves = []
    given=False
    for i in range(1, len(sys.argv)):
        if len(sys.argv[i])==64:
            BOARD=sys.argv[i]
        elif sys.argv[i] in tokens:
            given=True
            tokenToPlay=sys.argv[i].lower()
        else:
            if len(sys.argv[i])==2 and sys.argv[i][0].lower() in cells:
                letterIndex=cells.find(sys.argv[i][0].lower())
                numIndex = int(sys.argv[i][1])
                boardIndex= (letterIndex)+(numIndex-1)*8
                #boardIndex = (letterIndex*8)+(numIndex-1)
                moves.append(boardIndex)
            elif '-' in sys.argv[i]:
                continue
            else:
                moves.append(int(sys.argv[i]))
    nonPeriodCt=0
    for i in BOARD:
        if i!='.':
            nonPeriodCt+=1
    if given==False:
        if nonPeriodCt%2==0: tokenToPlay='x'
        else: tokenToPlay='o'
    tmpBoard=BOARD.lower()
    showSolution(tokenToPlay, tmpBoard)
main()