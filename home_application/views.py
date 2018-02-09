# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making 蓝鲸智云(BlueKing) available.
Copyright (C) 2017 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License.
"""

from common.mymako import render_mako_context, render_json
from blueking.component.shortcuts import get_client_by_request
from conf.default import APP_ID, APP_TOKEN
from common.log import logger
import logging
import sys


formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
console_handler = logging.StreamHandler(sys.stdout)
console_handler.formatter = formatter
logger.addHandler(console_handler)
logger.setLevel(logging.DEBUG)


def home(request):
    """
    首页
    """
    return render_mako_context(request, '/home_application/home.html')


def dev_guide(request):
    """
    开发指引
    """
    return render_mako_context(request, '/home_application/dev_guide.html')


def contactus(request):
    """
    联系我们
    """
    return render_mako_context(request, '/home_application/contact.html')


def get_ip(request):
    client = get_client_by_request(request)
    kwargs = {
        "app_code": APP_ID,
        "app_secret": APP_TOKEN,
        "app_id": 1,
        "bk_token": request.COOKIES['bk_token']
    }
    result = client.bhcp.get_ip(kwargs)
    data = result['data']
    # print result
    # print request.COOKIES
    # print request.COOKIES['bk_token']
    return render_json({"is_success": "one", "query_list": data})


def enter_ip(request):
    data = request.POST.get("data")
    client = get_client_by_request(request)
    logger.debug(data)
    exist_ = []
    new_host_list = []
    for item in eval(data):
        ip = item['ip']
        os_type = item['os_type']

        # 通过IP获取app_id
        kwargs = {
            "app_code": APP_ID,
            "app_secret": APP_TOKEN,
            "ips": ip,
            "bk_token": request.COOKIES['bk_token']
        }
        result = client.cc.get_host_company_id(kwargs)
        if result['data']:
            # 获取app_id字段
            app_id =result['data'][ip]["101"]["ApplicationID"]
            # 对比phone_num字段
            # 通过ip,app_id查询主机信息
            kwargs = {
                "app_code": APP_ID,
                "app_secret": APP_TOKEN,
                "ip": ip,
                "bk_token": request.COOKIES['bk_token'],
                "app_id": app_id,
            }
            result = client.cc.get_host_list_by_ip(kwargs)
            # 获取cmdb中该主机的phone_num字段
        else:
            # 新增数据，放入新增列表中
            new_host_list.append({"ip": ip, "os_type": os_type})

    if new_host_list:
        # for item in new_host_list:
        #     kwargs = {
        #         "app_code": APP_ID,
        #         "app_secret": APP_TOKEN,
        #         "ips": item['ip'],
        #         "bk_token": request.COOKIES['bk_token'],
        #         "os_type": item['os_type'],
        #     }
        # result = client.cc.enter_ip(kwargs)
        # logger.info(result)
        new_message = u"新增" + str(len(new_host_list)) + u"台主机"

    else:
        new_message = u"没有新增主机"
    logger.info(new_message)

    return render_json({"new_message": new_message, "new_host_list": new_host_list, "update_message": "2222"})


def do_enter_ip(request):
    data = request.POST.get("data")
    client = get_client_by_request(request)
    logger.debug(data)
    for item in eval(data):
        kwargs = {
            "app_code": APP_ID,
            "app_secret": APP_TOKEN,
            "ips": item['ip'],
            "bk_token": request.COOKIES['bk_token'],
            "os_type": '\"' + item['os_type'] + '\"',
        }
        logger.debug(item['os_type'])
        result = client.cc.enter_ip(kwargs)
        logger.debug(result)
    return render_json(result)


