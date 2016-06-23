#!/usr/bin/env python
# encoding: utf-8

from pandas import HDFStore


def page_view_stat(page_view_data):
    """ 点击量清单统计 """

    # 统计总体情况
    g = page_view_data.groupby(['dev_id', 'post_id'])
    d = g[['stat_view', 'stat_click']].sum()
    d['days'] = g['stat_date'].nunique()

    # 统计type=1
    c1 = page_view_data['type'] == 1
    g1 = page_view_data[c1].groupby(['dev_id', 'post_id'])
    d1 = g1[['stat_view', 'stat_click']].sum()
    d1['days'] = g1['stat_date'].nunique()

    # 统计type=2
    c2 = page_view_data['type'] == 2
    g2 = page_view_data[c2].groupby(['dev_id', 'post_id'])
    d2 = g2[['stat_view', 'stat_click']].sum()
    d2['days'] = g2['stat_date'].nunique()

    # 合并结果集
    d = d.join(d1, rsuffix=('_1'))
    d = d.join(d2, rsuffix=('_2'))
    d = d.fillna(0)
    d = d.reset_index()

    # 返回结果
    return d


def removeDataFrame(dfName):
    dbName = 'db.h5'
    s = HDFStore(dbName)
    if s.get_node(dfName):
        s.remove(dfName)
    s.close()

"""
xcols = [
    'stat_view', 'stat_click', 'stat_view_1', 'stat_click_1', 'stat_view_2', 'stat_click_2',
    'ucnt1', 'upct1', 'ucnt2', 'upct2', 'pcnt1', 'ppct1', 'pcnt2', 'ppct2', 'rela_p1_cnt', 'rela_p2_cnt',
]
"""
"""
xcols = [
    'ucnt1', 'upct1', 'ucnt2', 'upct2', 'pcnt1', 'ppct1', 'pcnt2', 'ppct2', 'rela_p1_cnt', 'rela_p2_cnt',
]
"""

xcols1 = [
    'ucnt1',
    # 'upct1',
    'pcnt1',
    # 'ppct1',
    # 'rela_p1_cnt',
]

xcols2 = [
    'ucnt2',
    'upct2',
    'pcnt2',
    'ppct2',
    'rela_p2_cnt',
]
