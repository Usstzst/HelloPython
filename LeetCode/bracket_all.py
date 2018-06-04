rows = [
'([<^>x[ ]{a}]{/}{t}g<^>)<{x}b>{x}<z({%}w >[b][c[c]]{<h>{h}}',
 '[/]{((x)({{*}*}w)w){f}{v}[%(^[z]{u}{ })([[ ]-]h)]{c}(*)[y]}',
 '<<(^)z>>[b]< >[[(c)u[v]{z<b< >><b>}]g][/b[(])v(v)(+)](v)',
 '[[b]][(v)g]<z>([{{<->+}e}[*]d<+>]g[[a] <+>(v){b}<e>]){a}[u]',
 '<h>(({-}b}a>)[(v)b]+(e{g})( )){< >(t[f])[w](f)<',
 '[^](<g{+}>[f{t}](d){x}^))%}<+{ (f)}>{}[ (u{]{{{d}^}x}',
 '((%)(f)[e][b[%][*]]u)([h] c})<b>[w]{<t>(/)(d)< >[%]%}',
 '<c>[w][[<t>+]]<{(t)a}d({<v>y<^{-}>}b)><w>{{%}^}',
 'b[u]<%>(%)(w))[y]{[u(f)]f< >}[<(>+]<w>(((<z> )(c)(b[w])/){ }h< >)',
 '([ ])<y><({{f}d}a(b)){/}*>{^}(/{h}{t[+]{t{b}}{x}[y]})',
 '< {^}>{+}{[a[e]]<z<^><%>{h}>{y}{(/((t a(t)))*( )}<a>( )}',
 '(<h>(<[d]g>(d)/c]<d>(d)[)(<[^]h>c)(<b> )){c}(b){ }',
 '{(h)[t][y]{%}{e}*(d)[*]}(e)<<(>{t}(z<+>)<[*]t>-(w)><-b)><[c]d[ ]>',
 '<a>{<(^)<h>c>[f]<h>{{v}y[/]}}((w{h})f)<{+}e( )>[t{w}]',
 '([v<%>>/)[+]<t]<<%>b>(({a<[x]*>{+[^]}}[w]h)< >)(h)',
 '<((*)f)((g(w[ [*]]))w{<y>+}(^))>{g}{+}{t}(h)',
 '<b><{{+}c{{(x)[x]f}^(^)}}[f](%)[u][u]<v>{<[z]e>f(g[%])}>',
 '[<<(+)( )y<*[u]>> ><h>[{ <y{v}>}^[c< >]{g}]<f><->[c<v>](/<z>)][t]',
 '(u[/])< >{e}<->{-}(( )[f]%)(d)[][[x[y]]t]{ {d{x}[t]}}{(b)x[z]}'
 ]
 
#row = '(u[/])< >{e}<->{-}(( )[f]%)(d)[][[x[y]]t]{ {d{x}[t]}}{(b)x[z]}'

# 存储左括号和又括号
open_brackets = '([{<'
close_brackets = ')]}>'
# 映射左右括号便于出栈判断
brackets_map = {')': '(', ']': '[', '}': '{', '>': '<'}

# 对于没一行数据，进行如下判定若括号为左括号，加入栈，若括号为右括号，判断是否跟栈尾括号对应，若对应，弹出栈尾元素，若所有括号均正确闭合，则最后栈为空。
for row in rows:
    stack = []
    balanced = True
    for char in row:
        if char in open_brackets:
            stack.append(char)
        elif char in close_brackets:
            if len(stack) < 1:
                balanced = False
                break
            elif brackets_map[char] == stack[-1]:
                stack.pop()
            else:
                balanced = False
                break
        else:
            continue
    if stack != []:
        balanced = False
    print(balanced)