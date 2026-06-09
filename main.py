import random

from astrbot.api import star
from astrbot.api.event import AstrMessageEvent, filter
from astrbot.core.star.filter.command import GreedyStr


def _do_choice(sender: str, options_str: str) -> str:
    options = options_str.strip().split()
    if len(options) < 2:
        return "请至少提供两个选项哦！"
    choice = random.choice(options)
    return f"帮 {sender} 选择了：{choice}"


class Main(star.Star):
    """帮我选 - 从多个选项中随机选择一个。

    用法: choice A B C 或 帮我选 A B C
    """

    @filter.command("choice")
    async def choice_cmd(self, event: AstrMessageEvent, *, rest: GreedyStr) -> None:
        yield event.plain_result(_do_choice(event.get_sender_name(), rest))

    @filter.command("帮我选")
    async def help_me_choose(self, event: AstrMessageEvent, *, rest: GreedyStr) -> None:
        yield event.plain_result(_do_choice(event.get_sender_name(), rest))
