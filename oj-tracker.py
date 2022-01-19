# -*- coding: UTF-8 -*-

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
        end_label="problems</div>")

def get_poj_ac_num():
    username = input(u"POJ 用户名：")
    return get_ac_num(
        url="http://poj.org/userstatus?user_id=" + username,
        start_label="<a href=status?result=0&user_id=" + username + ">")

# def get_luogu_ac_num() :
#     username = input(u"Luogu 用户编号：")
#     return get_ac_num(
#         url="https://www.luogu.com.cn/user/" + username,
#         start_label="<span data-v-d481ae34="" class=\"value\">",
#         end_label="</")

def get_nowcoder_ac_num() :
    username = input(u"nowcoder 用户编号：")
    return get_ac_num(
        url="https://ac.nowcoder.com/acm/contest/profile/" + username + "/practice-coding",
        start_label="<div class=\"state-num\">",
        end_label="</div>"
    )

def get_zoj_ac_num():
    username = input(u"ZOJ User ID（User Status 页面 URL 最后的那个数字）：")
    return get_ac_num(
        url="http://acm.zju.edu.cn/onlinejudge/showUserStatus.do?userId=" + username,
        start_label="AC Ratio:</font> <font color=\"red\" size=\"4\">",
        end_label="/")

def get_fzu_ac_num():
    username = input(u"FZU 用户名：")
    return get_ac_num(
        url="http://acm.fzu.edu.cn/user.php?uname=" + username,
        start_label="Total Accepted</td>",
        add=7)

def get_sgu_ac_num():
    username = input(u"SGU User ID：")
    return get_ac_num(
        url="http://acm.sgu.ru/teaminfo.php?id=" + username,
        start_label="Accepted: ")


def get_spoj_ac_num():
    username = input(u"SPOJ 用户名：")
    return get_ac_num(
        url="http://www.spoj.com/users/" + username + "/",
        start_label="<td><b>")


def get_tju_ac_num():
    username = input(u"TJU 用户名：")
    return get_ac_num(
        url="http://acm.tju.edu.cn/toj/user_" + username + ".html",
        start_label="Total Solved:</font> ",
        end_label="&")


def get_hnu_ac_num():
    username = input(u"HNU 用户名：")
    return get_ac_num(
        url="http://acm.hnu.cn/online/?action=user&type=status&id=" + username,
        start_label="Accepts : <a href=\"./?action=status&userid=" + username + "&judgeresult=0\">")


def get_acdream_ac_num():
    username = input(u"ACdream 用户名：")
    return get_ac_num(
        url="http://acdream.info/user/" + username,
        start_label="Solved: <span class=\"user user-green\">")


def get_uva_ac_num():
    username = input(u"UVa User ID（uHunt URL 最后的那个数字）：")
    return get_ac_num(
        url="http://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_authorstats&userid=" + username,
        start_label="<td width=\"20%\" align=\"center\"><h1 style=\"margin-top:-20px;margin-bottom:-5px;\">",
        loop=3)


def get_uvalive_ac_num():
    username = input(u"UVALive User ID（获取方法见 http://www.ahmed-aly.com/HowToGetLAUserID.jsp）：")
    return get_ac_num(
        url="https://icpcarchive.ecs.baylor.edu/index.php?option=onlinejudge&page=show_authorstats&userid=" + username,
        start_label="<td width=\"20%\" align=\"center\"><h1 style=\"margin-top:-20px;margin-bottom:-5px;\">",
        loop=3)

def main() :
    ac_nk = get_nowcoder_ac_num()
    ac_cf = get_cf_ac_num()
    ac_poj = get_poj_ac_num()
    ac_zoj = get_zoj_ac_num()
    ac_fzu = get_fzu_ac_num()
    ac_uva = get_uvalive_ac_num()
    ac_tju = get_tju_ac_num()
    ac_acdream = get_acdream_ac_num()
    ac_spoj = get_spoj_ac_num()
    ac_hnu = get_hnu_ac_num()
    ac_sgu = get_sgu_ac_num()
    # ac_luogu = get_luogu_ac_num()
    ac_cnt = ac_cf + ac_poj + ac_nk + ac_zoj + ac_fzu + ac_uva + ac_tju + ac_acdream + ac_spoj + ac_hnu + ac_sgu
    print(u"总 AC 数：%d" % ac_cnt)
    jud = input(u"是否查询Rating?(y/n):")
    if jud == 'y':
        get_cf_rank()
    n = input(u"按回车退出")

if __name__ == '__main__':
    main()
