from browser import document, html

def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)

# FizzBuzzの結果を格納するリスト
results = [fizzbuzz(i) for i in range(1, 101)]

# 結果をカンマ区切りの文字列に変換
result_string = ", ".join(results)

# 結果をdocumentに追加
document <= "FizzBuzz結果："
document <= html.BR()
document <= result_string

# 長い文字列を折り返して表示したい場合は、以下のようにdivを使用できます
# div = html.DIV(result_string)
# div.style = {"word-wrap": "break-word"}
# document <= div