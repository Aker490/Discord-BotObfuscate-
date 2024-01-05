import discord, config
from discord.ext import commands
from random import randint, choice, shuffle
from binascii import hexlify
from py_compile import compile
import io
import os
import shutil

from keep_alive import keep_alive
keep_alive()

strings = "abcdefghijklmnopqrstuvwxyz0123456789"

class Kyrie(commands.Cog):
    @staticmethod
    def encrypt(e: str):
        e = Kyrie._ekyrie(e)
        return Kyrie._encrypt(e)

    @staticmethod
    def decrypt(e: str):
        text = Kyrie._decrypt(e)
        return Kyrie._dkyrie(text)

    @staticmethod
    def _ekyrie(text: str):
        r = ""
        for a in text:
            if a in strings:
                a = strings[strings.index(a) - 1]
            r += a
        return r

    @staticmethod
    def _dkyrie(text: str):
        r = ""
        for a in text:
            if a in strings:
                i = strings.index(a) + 1
                if i >= len(strings):
                    i = 0
                a = strings[i]
            r += a
        return r

    @staticmethod
    def _encrypt(text: str, key: str = None):
        if type(key) == str:
            key = sum(ord(i) for i in key)
        t = [chr(ord(t) + key) if t != "\n" else "ζ" for t in text]
        return "".join(t)

    @staticmethod
    def _decrypt(text: str, key: str = None):
        if type(key) == str:
            key = sum(ord(i) for i in key)
        return "".join(chr(ord(t) - key) if t != "ζ" else "\n" for t in text)

class Key(commands.Cog):
    @staticmethod
    def encrypt(e: str, key: str):
        e1 = Kyrie._ekyrie(e)
        return Kyrie._encrypt(e1, key=key)

    @staticmethod
    def decrypt(e: str, key: str):
        text = Kyrie._decrypt(e, key=key)
        return Kyrie._dkyrie(text)

def ran_int(min: int = 3, max: int = 1000000):
    return randint(min, max + 1)

def Xe4a1(content: str, key: int) -> str:
    _content_ = Key.encrypt(content, key=key)
    _lines_sep_ = '/'

    content = _lines_sep_.join(hexlify(x.encode()).decode() for x in _content_)

    _names_ = ["_eval", "_exec", "_byte", "_bytes", "_bit", "_bits", "_system", "_encode", "_decode", "_delete",
               "_exit", "_rasputin", "_Xe4a1"]
    _names_ = ["self." + name for name in _names_]
    shuffle(_names_)

    for k in range(12):
        globals()[f'n_{str(k + 1)}'] = _names_[k]

    _types_ = ("str", "float", "bool", "int")

    def _find(chars: str):
        return "+".join(f"_n7_[{list('abcdefghijklmnopqrstuvwxyz0123456789').index(c)}]" for c in chars)

    _1_ = fr"""_n5_""", fr"""lambda _n9_:"".join(__import__(_n7_[1]+_n7_[8]+_n7_[13]+_n7_[0]+_n7_[18]+_n7_[2]+_n7_[8]+_n7_[8]).unhexlify(str(_n10_)).decode()for _n10_ in str(_n9_).split('{_lines_sep_}'))"""
    _2_ = fr"""_n6_""", r"""lambda _n1_:str(_n4_[_n2_](f"{_n7_[4]+_n7_[-13]+_n7_[4]+_n7_[2]}(''.join(%s),{_n7_[6]+_n7_[11]+_n7_[14]+_n7_[1]+_n7_[0]+_n7_[11]+_n7_[18]}())"%list(_n1_))).encode(_n7_[20]+_n7_[19]+_n7_[5]+_n7_[34])if _n4_[_n2_]==eval else exit()"""
    _3_ = fr"""_n4_[_n2_]""", fr"""eval"""
    _4_ = fr"""_n1_""", fr"""lambda _n1_:exit()if _n7_[15]+_n7_[17]+_n7_[8]+_n7_[13]+_n7_[19] in open(__file__, errors=_n7_[8]+_n7_[6]+_n7_[13]+_n7_[14]+_n7_[17]+_n7_[4]).read() or _n7_[8]+_n7_[13]+_n7_[15]+_n7_[20]+_n7_[19] in open(__file__, errors=_n7_[8]+_n7_[6]+_n7_[13]+_n7_[14]+_n7_[17]+_n7_[4]).read()else"".join(_n1_ if _n1_ not in _n7_ else _n7_[_n7_.index(_n1_)+1 if _n7_.index(_n1_)+1<len(_n7_)else 0]for _n1_ in "".join(chr(ord(t)-{key})if t!="ζ"else"\n"for t in _n5_(_n1_)))"""
    _5_ = fr"""_n7_""", fr"""exit()if _n1_ else'abcdefghijklmnopqrstuvwxyz0123456789'"""
    _6_ = fr"""_n8_""", fr"""lambda _n12_:_n6_(_n1_(_n12_))"""
    _all_ = [_1_, _2_, _3_, _4_, _5_, _6_]

    shuffle(_all_)

    _vars_content_ = ",".join(s[0] for s in _all_)
    _valors_content_ = ",".join(s[1] for s in _all_)
    _vars_ = _vars_content_ + "=" + _valors_content_
    _final_content_ = fr"""class Xe4a1():
 def __decode__(self:object,_execute:str)->exec:return(None,_n8_(_execute))[0]
 def __init__(self:object,_n1_:{choice(_types_)}=False,_n2_:{choice(_types_)}=0,*_n3_:{choice(_types_)},**_n4_:{choice(_types_)})->exec:
  {_vars_}
  return self.__decode__(_n4_[(_n7_[-1]+'_')[-1]+_n7_[18]+_n7_[15]+_n7_[0]+_n7_[17]+_n7_[10]+_n7_[11]+_n7_[4]])
Xe4a1(_n1_=False,_n2_=False,_sparkle='''{content}''')""".strip().replace("_n1_", n_1.removeprefix("self.")).replace("_n2_", n_2.removeprefix("self.")).replace("_n3_", n_3.removeprefix("self.")).replace("_n4_", n_4.removeprefix("self.")).replace("_n5_", n_5).replace("_n6_", n_6).replace("_n7_", n_7).replace("_n8_", n_8).replace("_n9_", n_9.removeprefix("self.")).replace("_n10_", n_10.removeprefix("self.")).replace("_n12_", n_12.removeprefix("self."))
    return _final_content_

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=intents)

XE4A1_SERVER = 1159165566217638040 # ไอดี เซิฟเวอร์ดิสคอส

XE4A1_VC = 1180152377890852994 # ไอดี ห้องที่จะให้บอทลง

@bot.event
async def on_ready():#---------------------------------------------------------------------------
    await bot.change_presence(activity=discord.Streaming(
    name="!obfuscate ตามด้วยไฟล์Python", url="https://www.twitch.tv/aker444a"))#---------------------------------------------------------------------------
    vc = discord.utils.get(bot.get_guild(XE4A1_SERVER).channels, id=XE4A1_VC)
    await vc.guild.change_voice_state(channel=vc,#---------------------------------------------------------------------------
                                      self_mute=False,
                                      self_deaf=True)
    print('''    
  ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
  █▄▀█▀▄██░▄▄▄██░▄░██░▄▄▀█▀░█
  ███░████░▄▄▄█░▀▀░▀█░▀▀░██░█
  █▀▄█▄▀██░▀▀▀████░██░██░█▀░▀
  ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
''')

@bot.command()
async def obfuscate(ctx, key: int = None):
    if key is None:
        key = ran_int(max=1000000)

    try:
        key = int(key)
    except ValueError:
        await ctx.send("Invalid key!")
        return

    if key < 3 or key > 1000000:
        await ctx.send("Invalid key!")
        return

    if not ctx.message.attachments:
        await ctx.send("Please attach a Python file for obfuscation.")
        return

    attachment = ctx.message.attachments[0]
    file_content = await attachment.read()

    original_filename = attachment.filename

    # Create a temporary directory for processing
    temp_dir = f"temp_{ctx.author.id}"
    os.makedirs(temp_dir, exist_ok=True)

    # Save the original file
    original_file_path = os.path.join(temp_dir, original_filename)
    with open(original_file_path, 'wb') as original_file:
        original_file.write(file_content)

    # Read the original content
    with open(original_file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # Obfuscate the content
    obfuscated_content = Xe4a1(content=content, key=key)

    # Create the obfuscated file
    obfuscated_filename = original_filename.removesuffix(".py") + "-obf.py"
    obfuscated_file_path = os.path.join(temp_dir, obfuscated_filename)
    with open(obfuscated_file_path, 'w', encoding='utf-8') as f:
        f.write(obfuscated_content)

    # Compile the obfuscated file
    compile(obfuscated_file_path)

    # Send the obfuscated file to the user
    obfuscated_file_data = io.BytesIO()
    with open(obfuscated_file_path, 'rb') as obfuscated_file:
        obfuscated_file_data.write(obfuscated_file.read())

    obfuscated_file_data.seek(0)
    await ctx.author.send(content=f"Obfuscated file with key {key}:", file=discord.File(obfuscated_file_data, obfuscated_filename))

    # Clean up temporary directory
    shutil.rmtree(temp_dir)

    await ctx.reply("Obfuscation complete!")

# ใส่ Token ของบอท Discord ที่นี่
bot.run(config.botToken)