import urllib.request as ur
import urllib.error as ue

def get_html_with_user_agent(url):
    user_agent = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
    headers = {'User-Agent': user_agent}
    request = ur.Request(url, headers=headers)
    try:
        response = ur.urlopen(request)
    except ue.HTTPError as err:  # urllib2.URLError
        # if err.code == 404:
        raise
    html = response.read()
    return html

def get_ac_num(url, start_label, end_label="<", loop=1, add=0):
    try:
        html = get_html_with_user_agent(url)
    except ue.HTTPError as err:
        if err.code == 404:
            print ("\t0")
            return 0
        else:
            raise

    start_position = 0
    for i in range(loop):
        start_position = html.find(start_label.encode(), start_position)
        if start_position == -1:  # not found this user or page error
            print ("\t0")
            return 0
        start_position += len(start_label)
    start_position += add

    jud_digit = html[start_position:start_position+1]
    while not jud_digit.isdigit():
        start_position += 1
        jud_digit = html[start_position:start_position+1]

    end_position = html.find(end_label.encode(), start_position)
    ac_num = int(html[start_position:end_position])
    print ("\t%d" % ac_num)
    return ac_num

def get_cf_rank():
    username = input(u"CF 用户名：")
    return get_ac_num(
        url="http://codeforces.com/profile/" + username,
        start_label="<span style=\"font-weight:bold;\" class=\"user-",
        end_label="</")


def get_cf_max():
    username = input(u"CF 用户名：")
    return get_ac_num(
        url="http://codeforces.com/profile/" + username,
        start_label="<span style=\"font-weight:bold;\" class=\"user-",
        end_label="</",
        add=100)

def get_cf_ac_num() :
    username = input(u"CF 用户名：")
    return get_ac_num(
        url="https://codeforces.com/profile/" + username,
        start_label="<div class=\"_UserActivityFrame_counterValue\">",
        end_label="problems</div>"
    )


def main() :
    ac_cf = get_cf_ac_num()

    ac_cnt = 0
    ac_cnt += ac_cf
    print(u"总 AC 数：%d" % ac_cnt)
    jud = input(u"是否查询Rating?(y/n):")
    if jud == 'y':
        get_cf_rank()
    n = input(u"按回车退出")

if __name__ == '__main__':
    main()
