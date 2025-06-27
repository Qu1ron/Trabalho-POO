
# Nesse arquivo temos uma biblioteca de ataques

Ataques = {
    'Fireball': {'Damage': 45, 'Mp': 20, 'Classe': 'Mago', 'Efeito': 'burn' },
    'Ice Spike': {'Damage': 55, 'Mp': 30, 'Classe': 'Mago', 'Efeito': 'freeze' },
    'Thunderbolt': {'Damage': 65, 'Mp': 40, 'Classe': 'Mago', 'Efeito': 'shocked' },
    'Hydro Pump': {'Damage': 70, 'Mp': 45, 'Classe': 'Mago', 'Efeito': 'soaked' },
    
    'Slash': {'Damage': 40, 'Mp': 15, 'Classe': 'Guerreiro', 'Efeito': 'bleed' },
    'Blade of Fate': {'Damage': 60, 'Mp': 35, 'Classe': 'Guerreiro', 'Efeito': 'Não sei' },
    'Last Bastion': {'Damage': 50, 'Mp': 25, 'Classe': 'Guerreiro', 'Efeito': 'Não sei' },

    'Double Shot' : { 'Damage': 38, 'Mp': 15, 'Classe': 'Arqueiro', 'Efeito': '?' },
    'Smoke Arrow' : { 'Damage': 48, 'Mp': 22, 'Classe': 'Arqueiro', 'Efeito': 'Blinded' },
    'Poison Arrow' : { 'Damage': 58, 'Mp': 30, 'Classe': 'Arqueiro', 'Efeito': 'Poisoned' },
}

mago_arte = """
NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNXOdc,','',,c0WMMMMMMMMMMMMMMMMMMMMMM
ldKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWK0KNWNXKkl:;,,,,';cdOXWMMMMMMMMMMMMMMMMMMMMMMM
c;;lkKWMMMMMMMMMMMMMMMMMMMMMMMN0dl:,c0Kd:;,'''''',l0NWMMMMMMMMMMMMMMMMMMMMMMMMMM
Od:.':xKNMMMMMMMMMMMMMMMMMMMW0o,'''.;Ox:;;,,,,,,,lKWMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MWKd;'',oXWMMMMMMMMMMMMMMMMNx,..',. .;,'''''''',lKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMNKOo;,:o0NWMMMMMMMMMMMMNd,...',...,,,,,,'''';kWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMWKd:',:d0WMMMMWNNWWNd,';:::;..',,,,,,,,;,oNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMNOl'.,oOkkkocccdd;.:dxkxc..'',,'''',:cOWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMW0l,',,''......',cdxdxl,','';::,',;xNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMWKd:,'........';:c::'.,,.'lddoo:;xNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMNKO:............','.';,;oxk00dlOXNXXXXXXXWMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMNXXXO:.   ....'''..''',;;clooddcldl::;;;;;:lx0XWMWWWMMMMMMMMMMMMMMM
MMMMMMMMMMMMMWXOl,'... ....',,''..''',,;;;;,'''...'.'..''',:oxdxXMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMW0xxxxc.......,,'..............'''''',''''''',;o0NMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMNOc'.....,;''..........',,'.....'',,:lodONWMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMN0xl'..',;,''''''',,,,............;clo0MMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMNkc'...,,,,,''..'...............'cONMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMXl'''.';,.....''''..'''',;ccok0NWMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMXl.'''...'''..;xOx:......,dKWMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMWO:..''.''...,xWMNkc,......lXMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMN0o,....'.....cKMMMNXOo;'...;d0XWMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMNd'............'dNMMMMMNX0o:,''.,dKWMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMWO;..............cXMMMMMMMMNXkc.. .cKWMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMXc............. .;OWMMMMMMMMMMNOo;;odx0NMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMWO;................;OWMMMMMMMMMMMWN0kocckXWMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMNo..................cKMMMMMMMMMMMMMMNK0kdoxKWMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMWk;..................'dNMMMMMMMMMMMMMMMMWNOddxkXWMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMXl....................lNMMMMMMMMMMMMMMMMMMMWXOxxx0NNXNWMM
MMMMMMMMMMMMMMMMMMMMMMWk;'...................cKWMMMMMMMMMMMMMMMMMMMMMWO:,::;:ok0
MMMMMMMMMMMMMMMMMMMMMWKc.'................';;,dXMMMMMMMMMMMMMMMMMMMMMMNkc,....',
MMMMMMMMMMMMMMMMMMMMMNo. .................,;,,,cOWMMMMMMMMMMMMMMMMMMMMMMKxlldol;
MMMMMMMMMMMMMMMMMMMMWOc,........................,dXWMMMMMMMMMMMMMMMMMMMMWN0000KK
MMMMMMMMMMMMMMMMMMMMKc........................',;,:OWMMMMMMMMMMMMMMMMMMMMMMNKK00
MMMMMMMMMMMMMMMMMMMNd;..........................'..,OWMMMMMMMMMMMMMMMMMMMMMMMMWN
MMMMMMMMMMMMMMMMMMKo;;..........................,;;,:0WMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMXd;,..........................;:,,,,ckNMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMWKo;;,...........................,,';;;,lKWMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMXOxl:,..,:,.......................':;..';;;:kNMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMWx'';,'.'kNd,ckOdol,',,,,,'''.,looxO0xl:,;;;';OMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMWk'.....cKWX0XMMMMN0OOOOOOOkkdxNMMMMMMWx'...'oXMMMMMMMMMMMMMMMMMMMMM
"""

guerreiro_arte = """
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNK0kdx0NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXKK0xollodONWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNOl::::ol;ldo0MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNd;:,.:; ,:,xMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMW0l:::ol:ldxXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMWNXXXXXNx;:dxkkk0XNXXXXXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMWNXK0OkkOxolol;,,;;:::ccclxkO000XWMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMXxlc:::cooollc;,,;;;;::;,,:odddoxKMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMWXKkc.. .',''',;:cccoxxo:'.,o0XXXWMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMWNk;     ..',;cccccldxdo:.'kWMMMMMMMMMMWWMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMNkc'.     ..',;:ccccclodd:..lx0WMMMMMMMMXKNMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMWNkc'..   .....',,;:cccloxd:.....:OKNMMMWXKxcoKMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMWx,...   .......',,;:cclodo;.  ...';kWWWXo,'.,OMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMWKl'. ............',,;:llooxOd,....',coool,...,OMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMWKd;...   ...........',:loollOMMXxl::::ccc::,,:lkXMMMMMMMMMMMMMMM
MMMMMMMMMMMMMWKo;....'''. ..........':loooll0MMMWNXXXXXXXXXKK00NWMMMMMMMMMMMMMMM
MMMMMMMMMMMMMNd'....',,;'...........,lolloolONMMMMMMMMMMWXXX0kk0KXXXXWMMMMMMMMMM
MMMMMMMMMMMMWO:......,,:,.......... .,lool;.'lKWMMMMMMMMMWWNOlokXWWWWMMMMMMMMMMM
MMMMMMMMMMMNO:......';;:,.......     ..,,'.  .l0WMMMMMMMMMMWOlokNMMMMMMMMMMMMMMM
MMMMMMMMMMMKc......',,''......   .','.     ..;cxNMMMMMMMMMMWOloONMMMMMMMMMMMMMMM
MMMMMMMMMMM0:.................  .,:c;.    .;cd0NWMMMMMMMMMMWOlo0WMMMMMMMMMMMMMMM
MMMMMMMMMMM0:................. .',:c:... .,:cdKWMMMMMMMMMMMWOlo0WMMMMMMMMMMMMMMM
MMMMMMMMMMKo,..................',;:c:'....,:cdKWMMMMMMMMMMMWOlo0WMMMMMMMMMMMMMMM
MMMMMMMMWXo'...................';:cc:'....':cdKWMMMMMMMMMMMWOloONMMMMMMMMMMMMMMM
MMMMMMMWXo'.................  .,:cc:,...   .;lOWMMMMMMMMMMMWOlokNMMMMMMMMMMMMMMM
MMMMMMWXd,..................  ..',,,......  ..lXMMMMMMMMMMMWOlokNMMMMMMMMMMMMMMM
MMMMMMXd,...................  ............  ..oNMMMMMMMMMMMWOlokNMMMMMMMMMMMMMMM
MMMMMXd,.......................,;:,........':d0WMMMMMMMMMMMWOllkNMMMMMMMMMMMMMMM
MMMMW0occc;'..............   .;;,'......  .:d0NMMMMMMMMMMMMWOllkNMMMMMMMMMMMMMMM
MMMMMWWWWWOc;;'...........   .,;'.......   ,o0WMMMMMMMMMMMMWOllkNMMMMMMMMMMMMMMM
MMMMMMMMMMWXXKkoooooc'....    ..........    .dWMMMMMMMMMMMMWOllkNMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMWX0OOOl..';:::::::cd;   'cOWMMMMMMMMMMMMWOllkNMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMO:,cONNNNNNNNW0o;.:xXMMMMMMMMMMMMMWOllkNMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMO;,oKMMMMMMMMMMM0:;dXMMMMMMMMMMMMMWOllkNMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMx.,OMMMMMMMMMMMMMO;cXMMMMMMMMMMMMMWOllkNMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMXo';dXMMMMMMMMMMMNx:ckKWMMMMMMMMMMMWOlokNMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMWk:;;:dXWMMMMMMMMM0occclkKXXNWMMMMMMWOlokNMMMMMMMMMMMMMMM
ddddddddddddddddddddddddc,''',:odddddddddl;,,,,,;;;codddddddc;;co0WMMMMMMMMMMMMM
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxKWMMMMMMMMMMMMM
"""


arqueiro_arte = """
...............';,'''';lkXWMMMMMMMMMMMMMMMWWWMMW0dl,','.','.....''.............'
.,.........''.,::::,;clkNMMMMMMMMMMMMMMMMM0o0MMWNX0dol;,,,''..,,,''.........,;,'
''''''',,''',;,,:ldxxOXNWMMMMMMMMMMMMMMMMWx'oWMMMWWWXOo::,''',,,,',,'',''..'.','
,,,,,,,,,,,;,,,,;xNWWNWMMMMMMMMMMMMMMMMWXOoc:oXMMMMMWNKxl:,,;,;,,,,,,,,,,,,'.'''
,,,'',,',;;:clc:;oXWMMMMMMMMMMMMMMMMMMXxokNWOccOWMMMMMW0l;:clc,;oc',,,,,,,,''',;
',;;,'',::::o0kodOXWMMMMWWNWNNWWMMMMMNxkXNMMM0,.oKWMMMMN0dok0k:l0dc:'',,'''',,;c
,:loo;,cldxdkNNXNWK0NMWKo;;:::cdONMMXxkNMMMMMN0c'lXMMMMMXO0NWXxxXKxo;'lx:''',:ol
:lONOcl0XNWNWNOxdoc,xW0,  ...'cc,dWNdxNMMMMMMMM0clONMMMMMMMMMWNWMWNXxcoOl',,,:ol
co0Nd,lXMMMNx:,,'..'xW0,  ..':odOKKkkXMMMMMMMMMMx:xKWMMMMMMMMMMMMMMMM0:;;,'',;;o
:ldxdkKWMMMNd..',;',dXWk' .,:xkkXKdOWMMMMMMMMMMMKl:dKMMMMMMWMMMMMMMMMWxl:,'',:lO
;:lkNMMMMMMMN0c':;...:c;'.,,':o0KdOWMMMMMMMMMMMMWo.cKMMMMMMWMMMMMMMMMN0Oc'',;:o0
,:kWMMMMMMMMMMO'..........''..,::l0XXNXXXXXNXXXXXl.c0XXXXXXXXXOOKNWMMWMXl''',:l0
;:OWMMMWWMMMMMKc..':clc,'''..'''..,:cccdkxocoxddd;.:dkkkkkkkkxc;ckNMMMMXl''',:l0
;cOWMWWX0XMMMMMk..cxxdc'..........,;;,,d0kc:ccc,,..cONMMMMMMWWX0O0NMMMMXl'',,:l0
;cOWMMW0x0WMMMMO'..','.  . ..'','.''.',:l:..'',::'.,OWMMMMMMMMMW0kONMMMXl',,;:lO
;:OWWWXkxk0NMMMNd.       ....,,;;':odOK0OxloO0KWWo.:0MMMMMMMMMWKkxxONWWKl'',;coO
;ckNNXOxxxkKWMMXo,.      ....',;:cd0NMMMMMMMMMMMWd':OWMMMMMMWWNOxxxkXWWKl'',:lo0
;cONNXOxxxOKWMXl... .   ....',;,'dKxkNMMMMMMMMMMNl;oKMMMMMMMWWN0kxxk0XX0c',,,coO
;ckXKOxxxxxx0Kl... ..   ....',,'.cO0xkNMMMMMMMMMx;o0NMWWWWMWWX0kxxxxk0KKl,,',:lk
;cxKKOxxxkkko:'.....    ..,'.....':0XxkNMMMMMWWXocxXWWWWMMWNXKOkkxxxO0K0c,'.,:lO
;ckKOkkxxkkl,''.....   . .'......'lKWKokNWMWNNNx,c0NWNXXWWNXKKOkxxxxkOK0c',',:lk
;cx0kkkxxo:'''.... .   .......',::;:kXKkdkXWNXk;,xNNWNOkXNXK0Okkxxxxxk00c',,,:co
;cdkkxxdl;,'........       ..';::;;::oKN0xdKKd:o0XNNWXOx0XX0kkkkxxxkkkkkc'',;:cx
cldxdl:;,'.........      ...';:cc:;;;;dXMNko,;xXXXWWXOkxx0K0kkOOkxxxxkkx:''';ccx
;;;;,,''..................,,,;cllc::;,c0WWk,c0NNNXNX0kxxkOOOkOOkkkxxxxkd:'',;::l
'''............';:lo,.......,;;;,,,'..,dOKx:xXKKXXKKOkxxxkkkOOkxxxxxxoxx:',,,,,l
;;............:dxkOO;     .;dkkx:. ...';cx000KKKKK0Okkxxxxxkkkxxxxxxdldd:','',:d
:c::,.......'oxxxxkx, ....c0KKKXKd;. ..',,o0XKKKK000Oxxxxkkkxxxxxddooolc;,,,',ld
;:okxdc,'';cdxxxxdc'.   .l0KKKNNKK0o. ....:OXKKKKK0Okxxxxxkxxxxxo;;coooooolc;;co
,;lkdcdkxdddxkxxd;.... .oKKKKKKKKKKx. ....,xKKKKKKK0kxxxoldxxdlc::clodddolll:;;c
,;:c;':llc:cokko,...',.,kK0KKKKKKKd...',,,'l0KXKK0Okxxxxxolol:;,:lc;:lol:;ccc:;;
::;........,lxko'......ckOO0KKKKKKo'.....''l0KKK0Okxxxxxxxc;::c;;;;,',,,,';:cccc
:;.........':dOl...'''okkkkOKKKKKKKx' ..';,l0KKKOkkxxxxxxl,';;,,,,'','....',,;:;
'.....',,,,';okc..'';dOkkxkO0KKKKKK0l. ..''l0K0Okxxxdolc:,,''''.','...........',
......,;:::,.'dl..';dkkkkkkk0KKKKKKK0o.....l00kxxxxd:,;;;,......,,....'.........
......',,,,..'c,..,cdkkkxddxkO00OOK0Ox'...';lddolod;....',''''.,;,,,....'...'.''
..  ........ .'. ...':;;:;lddc:lccdl;;.  ....',,,,::,;;,,',;ccllc,,,',c:,;c:'.,:
;,;;::;;;,,,,;;;;;;,;;;,,;coc;;::::;;;;,;;;;;;;:::cooddollodoodddllollddoodoolco
ldoolccllllc:clodlc,clc;:ccc::lddoccllllclc:ldcclodc;lc:ollc:looc;cloc:::ll:cl:c
:cc;,..'.;'.',.';...''..',,'.':cc,..,'......,;''',:'.,,,,.''.,c:''',,...',..';'.
"""

mago_inv_arte = """
MMMMMMMMMMMMMMMMMMMMMMW0c,,'',',cdOXNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN
MMMMMMMMMMMMMMMMMMMMMMMWXOdc;',,,,;:lkKNMWNK0KWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKdl
MMMMMMMMMMMMMMMMMMMMMMMMMMWN0l,'''''',;dOK0c,:ld0WMMMMMMMMMMMMMMMMMMMMMMMWKkl;;c
MMMMMMMMMMMMMMMMMMMMMMMMMMMMWKl,,,,,,,;:cxO;.''',o0WMMMMMMMMMMMMMMMMMMMNKx:'.:dO
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKl,'''''''',;. .,'..,xNMMMMMMMMMMMMMMMMWXo,'';dKWM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWk;'''',,,,,,...,'...,dNMMMMMMMMMMMMWN0o:,;oOKNMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNo,;,,,,,,,,'..;:::;',dNWWNNWMMMMW0d:,':dKWMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWOc:,''',,,''..cxkxd:.;ddcccokkkOo,.'lONMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNx;,',:;,'',',lxdxdc,'......'',,',l0WMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNx;:oodl:'.,,.'::c:;'........',:dKWMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMWXXXXXXXNXOld00koc;,;'.','............:OKNMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMWWWMWX0xl:;;;;;::ldlcddollc;;,'''..'''....   .:OXXXNMMMMMMMMMMMMM
MMMMMMMMMMMMMMMXxdxo:,'''.''.'...''',;;;,,,'''..'',,'.... ...',lOXWMMMMMMMMMMMMM
MMMMMMMMMMMMMMMN0o;,'''''',,'''''...............',,.......cxxxx0WMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMWNOdol:,,''.....',,'..........'';,.....'cONMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMM0olc;............,,,,''''''',,,'..'lx0NMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMNOc'...............'.''',,,,,...'ckNMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMWN0xocc;,''''..''''.....,;'.'''lXMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMWKd,......:xOx;.''''...'''.lXMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMXl......,ckNMWx,...''.''..:OWMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMWX0d;...';oOXNMMMKc.....'....,o0NMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMWKd,.'',:o0XNMMMMMNd'............'dNMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMWKc. ..ckXNMMMMMMMMXl..............;OWMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMN0xdo;;oONMMMMMMMMMMWO;...............cXMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMWXkccok0NWMMMMMMMMMMMWO;... ............;OWMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMWKxodk0KNMMMMMMMMMMMMMMKc.... .............oNMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMWXkxddONWMMMMMMMMMMMMMMMMNd'..................;kWMMMMMMMMMMMMMMMMMMMMMMM
MMWNXNN0xxxOXWMMMMMMMMMMMMMMMMMMMNl....................lXMMMMMMMMMMMMMMMMMMMMMMM
0ko:;::,:0WMMMMMMMMMMMMMMMMMMMMMWKc...................';kWMMMMMMMMMMMMMMMMMMMMMM
,'....,ckNMMMMMMMMMMMMMMMMMMMMMMXd,;;'................'.cKWMMMMMMMMMMMMMMMMMMMMM
;lodllxKMMMMMMMMMMMMMMMMMMMMMMWOc,,,;,................. .oNMMMMMMMMMMMMMMMMMMMMM
KK0000NWMMMMMMMMMMMMMMMMMMMMWXd,........................,cOWMMMMMMMMMMMMMMMMMMMM
00KKNMMMMMMMMMMMMMMMMMMMMMMWO:,;,'........................cKMMMMMMMMMMMMMMMMMMMM
NWMMMMMMMMMMMMMMMMMMMMMMMMWO,..'..........................;dNMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMW0:,;;,..........................;;oKMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMNkc,,,,:;..........................,;dXMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMWKl,;;;',,...........................,;;oKWMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMNk:;;;'..;:'.......................,:,..,:lxOXMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMO;';;;,:ox0Oxool,.''',,,,,',codOkc,dNk'.',;''xWMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMXo,...'xWMMMMMMNxdkOOOOOOOO0NMMMMX0XWKc.....'kWMMMMMMMMMMMM
"""

guerreio_inv_arte = """
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN0xkO0KNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNOdlllox0KKXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM0odllxo::::lONMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMx,:,;d:.,:;dNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXxdllxo:::l0WMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXXXXXNX0kkxxd:;xNXXXXXNWMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMWX000Okxlccc::;;;,,;loloxOkkOOKXNWMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMKxodddo:,,;::;;;;,,;clloooc:::clxXMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMWXXX0o,.':oxxoccc:;,''','. ..ckKXWMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMWWMMMMMMMMMMWk'.:odxdlccccc;,'..     ;kXWMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMNKXMMMMMMMMW0xl..:ddolccccc:;,'..     .'ckNMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMKocxKXWMMMNKO:.....:dxolccc:;,,'.....   ..'ckNWMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMO,.',oXWWWk;'...  .;odolcc:;,,'.......   ...,xWMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMO,...,loooc,'....,dOxool:;;,,'............ .'l0WMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMXkl:,,::ccc::::lxXMMOllolc:,'...........   ...;dKWMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMWN00KKXXXXXXXXXNWMMM0lloool:'.......... .'''....;oKWMMMMMMMMMMMMM
MMMMMMMMMMWXXXXK0kk0XXXWMMMMMMMMMMNOloollol,...........';,,'....'dNMMMMMMMMMMMMM
MMMMMMMMMMMWWWWXkolONWWMMMMMMMMMWKl'.;lool,. ..........,:,,......:OWMMMMMMMMMMMM
MMMMMMMMMMMMMMMNkolOWMMMMMMMMMMW0l.  .',,..     .......,:;;'......:ONMMMMMMMMMMM
MMMMMMMMMMMMMMMNOolOWMMMMMMMMMMNxc;..     .','.   ......'',,'......cKMMMMMMMMMMM
MMMMMMMMMMMMMMMW0olOWMMMMMMMMMMWN0dc;.    .;c:,.  .................:0MMMMMMMMMMM
MMMMMMMMMMMMMMMW0olOWMMMMMMMMMMMWKdc:,.....:c:,'. .................:0MMMMMMMMMMM
MMMMMMMMMMMMMMMW0olOWMMMMMMMMMMMWKdc:,....':c:;,'..................,oKMMMMMMMMMM
MMMMMMMMMMMMMMMNOolOWMMMMMMMMMMMWKdc:'....':cc:;'...................'oXWMMMMMMMM
MMMMMMMMMMMMMMMNkolOWMMMMMMMMMMMWOl;.  ....,:cc:,.  .................'oXWMMMMMMM
MMMMMMMMMMMMMMMNkolOWMMMMMMMMMMMXl..  ......,,,'..  ..................,dXWMMMMMM
MMMMMMMMMMMMMMMNkolOWMMMMMMMMMMMNo..  ............  ...................,dXMMMMMM
MMMMMMMMMMMMMMMNkllOWMMMMMMMMMMMW0d:'........,:;,.......................,dXMMMMM
MMMMMMMMMMMMMMMNkllOWMMMMMMMMMMMMW0d:. .......',;;.   ..............';ccco0WMMMM
MMMMMMMMMMMMMMMNkllOWMMMMMMMMMMMMW0o,  ........';,.   ...........';;cOWWWWWMMMMM
MMMMMMMMMMMMMMMNkllOWMMMMMMMMMMMMWd.   ...........    ....,coooookKXXWMMMMMMMMMM
MMMMMMMMMMMMMMMNkllOWMMMMMMMMMMMMWOc'  ;xdc:::::::;'..lOOO0XWMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMNkllOWMMMMMMMMMMMMMXx:.;0WWNNNNNNNNOc,:OMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMNkllOWMMMMMMMMMMMMMXd;:0MMMMMMMMMMMKo,;OMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMNkllOWMMMMMMMMMMMMMXc;OMMMMMMMMMMMMMO,.xMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMNkolOWMMMMMMMMMMMWKkc:xNMMMMMMMMMMMXd;'oXMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMNkolOWMMMMMMWNXXKklccco0MMMMMMMMMWXd:;;:kWMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMW0oc;;cdddddddoc;;;,,,,,;ldddddddddo:,''',cdddddddddddddddddddddddd
MMMMMMMMMMMMMWKxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
"""

arqueiro_inv_arte = """
'.............''.....','.',';lx0WMMWWWMMMMMMMMMMMMMMMWXkl;'''',;'...............
',,,.........'',,'..'',,,;lox0XNWMM0d0MMMMMMMMMMMMMMMMMNOoc;,;cc:,.''.........'.
','.'..'','',,',,,,''',:coOXWWWMMMWd,xWMMMMMMMMMMMMMMMMWWXOxxdl:;,,,''',,'''''''
'''.',,,,,,,,,,,,;,;;,:lxKWWMMMMMKd:cd0WMMMMMMMMMMMMMMMMMWWWWXx:,,,,;;,,,,,,,,,,
;,''',,,,,,,,,co;,:lc::l0WMMMMMWOlcONNOk0NMMMMMMMMMMMMMMMMMMWKd::ccc:;;,'','',,,
c;,,,'',,,',:cxOocx0kdd0NMMMMWKo';0MMMNOdkNMMMMMWWNNNNWWMMMMWXOxdkOo::::,'',;,,'
lo:,,,':dl,;oxKXkkXWN0OXMMMMMXo,l0WMMMMNKkkXMMNOdccc:::oKWMNKXNNXNNkdxdlc,;lol:,
lo:,,,'lkolkKNWMWNWMMMMMMMMMNOllKMMMMMMMMNkxNWx;::,... .;0Wx;codxONWNWNX0lcONOl:
o:;,'',;:c0MMMMMMMMMMMMMMMMWKx:xWMMMMMMMMMXOOKKOxo:'..  ;0Wx,..',;:kNMMMXo;dX0oc
Ol:,'',:lkNMMMMMMMMMMMMMMMMKdclKMMMMMMMMMMMWOxKXkkd:,..'kNKd,,;,'.'dNMMMWKkdxdl:
0o:;,''lOKNMMMMMMMMMMMMMMMMKc'oWMMMMMMMMMMMMWOx0Oo:',,.';c:..';;,c0NMMMMMMMNOl:;
0o:,'''oXMWMMWNKOOXNNXXNNNN0l'lXNNNNNNNNNXXNXOl::,..''..........,OMMMMMMMMMMWk:;
Oo:,'',oXMMMMNkc;cxOkkkkOOkd:.;dddxoloxdlccc:,..'''...'',clc:'..cXMMMMMWWMMMWO:;
Oo:,'''oXMMMWN0OKXWWMMMMMMWO:..',:c::cxo;,,;;,..........'cdxdc..kMMMMMX0XWMMWOc;
Ol:;,,'lXMMWNOk0WMMMMMMMMMWO;.'::,''.'::;,'.''.',''.. .  .'''..'OMMMMW0k0WMMWOc;
Ooc;,''lKMWNOxxkXWMMMMMMMMM0:'oWWXKOdox0KKOdo:,;;,,....      .'dNMMMN0kxOXWWWO:;
Ool:,''lKWWXOxxk0NWWMMMMMMWO:,dWMMMMMMMMMMMN0xl;;,'.....     .,oXMMWKkxxkOXNXOc:
Ooc;,,'c0XX0kkxk0NWWMMMMMMMKo;oXMMMMMMMMMMNOkKd',;,.....   . ...lXMWKOxxkOXNXOc;
kl:,',,l0K0kxxxkk0XWWMWWWWMN0o:xWMMMMMMMMNkx0Oc''','....   ......lK0kxxxxkOKXkc;
kl:,'',l0K0OkxxkkOKXNWMMWWWWXkcoXMWMMMMNKkkX0c'.....',..    .....,:oxkkxxkOKKxc;
kl:,',,lOKOkxxxkkOKKXNWWXXNWN0l,xNNNWMWOldKW0l''.....'...   .....'';lxkxxkk00xc;
oc:;,,,lO0kxxxxxkkO0KXNXOONWNXx;;kXNWXOk0KXOc;::,'.......   ......'',:oxxkkO0xc;
xc:;,',cxkkkkxxxkkkO0XX0kOXWWNX0o:dKKxkXWKo::;;::;'..       ........',;ldxxkkdc;
xcc;,'':dkkxxxxkOOkO0K0kxkOXWWXXXx;;oONX0d;,;;:cc:;'...      .........',;:ldxdlc
l::;,'':dkxxxxxkkOOkOOOkxxk0XNNNNX0l;kW0dc,;::clcc;,,'..................'',,;;;;
l;,,,,':xxddxxxxxkOOkkkxxxkOKKXXKKXxck0dc,..',,,;:;,.......,ol:;'.............''
o:,'',,:ddodxxxxxxkkkxxxxxkkO0KKKKKK00x:''... .:dkkd;.     ;kOkxo:............;;
dl,',,,;cloooddxxxxxkkkxxxkO000KKKKX0o;'... .;d0XKKKOc.... ,xkxxxxl'.......,::c:
oc;;clloooooc;;oxxxxxxxxxxxkO00KKKKXO:.... .o0KXNXKKKOl.   .'cdxxxxdc;'',:oxxo:;
c;;:cloodddolc::cldxxdldxxxk0KKKKKKKx;.... .d0KKXKKKKK0o. ....;dkkkxdodxxoldxl;,
;;:ccc;:lll::cc:;;cloloxxxxxkO0KKXK0l,,''...'o0KKKKKKK0x;.,'...,okkocccll:';c:;,
cccc:;'',,,',,;;;c::;cdxxxxxxkO0KKK0l,'.....'o0KKKKK00Okc'.....,okxl,........;::
;:;,,'....'''',',;;;,,ldxxxxxkkOKKK0l;,....'xKKKKKKKOOkkkl,''..'lkd:'.........;:
,'...........','.','',,:clodxxkkO0K0l'... .l0KKKKKK0Okkkkkd;''..cxo;',,,,'.....'
.........'....,,......,;;;,:dxxxxO00l'.. .l0KKKKKKK0Okxkkkkd:'..lo,.,:::;,......
''.'...'....',,;,.''',,'....:ooloddl;'.. ,dO00OO00Okkddxxxxoc,..,c'..,,,,'......
:,.':c;,::,',,;cllcc;,,,,;;,::,,;,'....  .,;loccl:cddl::;;:'.....'........... ..
olloodooodllolloddoodolloddooc:::;;;;;;,,;;;;::::;;clc;,,;;;,;;;;;,,,,,;;;::;;;;
cclc:ll:::colc:cool:clloccl:coolccol::cclclcccoddl:::c::;cl:,cloolc:cclllccloodl
.';'..,....,,''':c,.''.,,,,.':;'',;,......''..,cc:'.',,'..''...;,.''.';''..,;cc:
"""