from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

from wechatpy import parse_message, create_reply
from wechatpy.utils import check_signature
from wechatpy.exceptions import InvalidSignatureException
from wechatpy.replies import BaseReply

TOKEN = 'dengzhouzhang'

@csrf_exempt
def handle_wx(request):
    # GET方式用于微信公众平台绑定验证
    if request.method == 'GET':
        signature = request.GET.get('signature', '')
        timestamp = request.GET.get('timestamp', '')
        nonce = request.GET.get('nonce', '')
        echo_str = request.GET.get('echostr', '')

        try:
            check_signature(TOKEN, signature, timestamp, nonce)
        except InvalidSignatureException:
            echo_str = 'error'
        response = HttpResponse(echo_str, content_type="text/plain")
        return response
    # POST方式用于接受和返回请求
    else:
        reply = None
        msg = parse_message(request.body)

		# 判断消息类型，文本消息则调用reply_text进行处理
        if msg.type == 'text':
            #reply = reply_text.do_reply(msg)
            reply = create_reply('文本消息' + msg.content, msg)
        elif msg.type == 'voice':
            #reply = reply_event.do_reply(msg)
            reply = create_reply('语音消息', msg)
        else:
            pass
        if not reply or not isinstance(reply, BaseReply):
            reply = create_reply('暂不支持您所发送的消息类型哟~ 回复“帮助”查看使用说明。', msg)

        response = HttpResponse(reply.render(), content_type="application/xml")
        return response