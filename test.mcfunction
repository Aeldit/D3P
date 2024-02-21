##
 # Description: Places a sign with the targeted armor stand's text and the selected color, then sets this text back on the armor stand
 # Called by:   #functions -> text_display/dye/ft_1_dark_red --- text_display/dye/ft_16_black
##
# Adds the selected tag to the targeted armor stand
tag @e[type=armor_stand,distance=..3,limit=1,sort=nearest] add sp_selected

# Sets the color on the sign's text
#ifdef MC_1_20_x
execute if entity @s[scores={ft_color=1}] run setblock ~ ~ ~ oak_sign{front_text: {messages: ['{"color":"dark_red","nbt":"CustomName","entity":"@e[tag=sp_selected]","interpret":true}', '{"text":""}', '{"text":""}', '{"text":""}']}}
execute if entity @s[scores={ft_color=2}] run setblock ~ ~ ~ oak_sign{front_text: {messages: ['{"color":"red","nbt":"CustomName","entity":"@e[tag=sp_selected]","interpret":true}', '{"text":""}', '{"text":""}', '{"text":""}']}}
execute if entity @s[scores={ft_color=3}] run setblock ~ ~ ~ oak_sign{front_text: {messages: ['{"color":"gold","nbt":"CustomName","entity":"@e[tag=sp_selected]","interpret":true}', '{"text":""}', '{"text":""}', '{"text":""}']}}
execute if entity @s[scores={ft_color=4}] run setblock ~ ~ ~ oak_sign{front_text: {messages: ['{"color":"yellow","nbt":"CustomName","entity":"@e[tag=sp_selected]","interpret":true}', '{"text":""}', '{"text":""}', '{"text":""}']}}
execute if entity @s[scores={ft_color=5}] run setblock ~ ~ ~ oak_sign{front_text: {messages: ['{"color":"dark_green","nbt":"CustomName","entity":"@e[tag=sp_selected]","interpret":true}', '{"text":""}', '{"text":""}', '{"text":""}']}}
execute if entity @s[scores={ft_color=6}] run setblock ~ ~ ~ oak_sign{front_text: {messages: ['{"color":"green","nbt":"CustomName","entity":"@e[tag=sp_selected]","interpret":true}', '{"text":""}', '{"text":""}', '{"text":""}']}}
execute if entity @s[scores={ft_color=7}] run setblock ~ ~ ~ oak_sign{front_text: {messages: ['{"color":"aqua","nbt":"CustomName","entity":"@e[tag=sp_selected]","interpret":true}', '{"text":""}', '{"text":""}', '{"text":""}']}}
execute if entity @s[scores={ft_color=8}] run setblock ~ ~ ~ oak_sign{front_text: {messages: ['{"color":"dark_aqua","nbt":"CustomName","entity":"@e[tag=sp_selected]","interpret":true}', '{"text":""}', '{"text":""}', '{"text":""}']}}
execute if entity @s[scores={ft_color=9}] run setblock ~ ~ ~ oak_sign{front_text: {messages: ['{"color":"dark_blue","nbt":"CustomName","entity":"@e[tag=sp_selected]","interpret":true}', '{"text":""}', '{"text":""}', '{"text":""}']}}
execute if entity @s[scores={ft_color=10}] run setblock ~ ~ ~ oak_sign{front_text: {messages: ['{"color":"blue","nbt":"CustomName","entity":"@e[tag=sp_selected]","interpret":true}', '{"text":""}', '{"text":""}', '{"text":""}']}}
execute if entity @s[scores={ft_color=11}] run setblock ~ ~ ~ oak_sign{front_text: {messages: ['{"color":"light_purple","nbt":"CustomName","entity":"@e[tag=sp_selected]","interpret":true}', '{"text":""}', '{"text":""}', '{"text":""}']}}
execute if entity @s[scores={ft_color=12}] run setblock ~ ~ ~ oak_sign{front_text: {messages: ['{"color":"dark_purple","nbt":"CustomName","entity":"@e[tag=sp_selected]","interpret":true}', '{"text":""}', '{"text":""}', '{"text":""}']}}
execute if entity @s[scores={ft_color=13}] run setblock ~ ~ ~ oak_sign{front_text: {messages: ['{"color":"white","nbt":"CustomName","entity":"@e[tag=sp_selected]","interpret":true}', '{"text":""}', '{"text":""}', '{"text":""}']}}
execute if entity @s[scores={ft_color=14}] run setblock ~ ~ ~ oak_sign{front_text: {messages: ['{"color":"gray","nbt":"CustomName","entity":"@e[tag=sp_selected]","interpret":true}', '{"text":""}', '{"text":""}', '{"text":""}']}}
execute if entity @s[scores={ft_color=15}] run setblock ~ ~ ~ oak_sign{front_text: {messages: ['{"color":"dark_gray","nbt":"CustomName","entity":"@e[tag=sp_selected]","interpret":true}', '{"text":""}', '{"text":""}', '{"text":""}']}}
execute if entity @s[scores={ft_color=16}] run setblock ~ ~ ~ oak_sign{front_text: {messages: ['{"color":"black","nbt":"CustomName","entity":"@e[tag=sp_selected]","interpret":true}', '{"text":""}', '{"text":""}', '{"text":""}']}}
#elseifdef MC_1_19_4
execute if entity @s[scores={ft_color=1}] run setblock ~ ~ ~ oak_sign{Text1: '{"color":"dark_red","nbt":"CustomName","entity":"@e[tag=sp_selected]","interpret":true}'}
execute if entity @s[scores={ft_color=2}] run setblock ~ ~ ~ oak_sign{Text1: '{"color":"red","nbt":"CustomName","entity":"@e[tag=sp_selected]","interpret":true}'}
execute if entity @s[scores={ft_color=3}] run setblock ~ ~ ~ oak_sign{Text1: '{"color":"gold","nbt":"CustomName","entity":"@e[tag=sp_selected]","interpret":true}'}
execute if entity @s[scores={ft_color=4}] run setblock ~ ~ ~ oak_sign{Text1: '{"color":"yellow","nbt":"CustomName","entity":"@e[tag=sp_selected]","interpret":true}'}
execute if entity @s[scores={ft_color=5}] run setblock ~ ~ ~ oak_sign{Text1: '{"color":"dark_green","nbt":"CustomName","entity":"@e[tag=sp_selected]","interpret":true}'}
execute if entity @s[scores={ft_color=6}] run setblock ~ ~ ~ oak_sign{Text1: '{"color":"green","nbt":"CustomName","entity":"@e[tag=sp_selected]","interpret":true}'}
execute if entity @s[scores={ft_color=7}] run setblock ~ ~ ~ oak_sign{Text1: '{"color":"aqua","nbt":"CustomName","entity":"@e[tag=sp_selected]","interpret":true}'}
execute if entity @s[scores={ft_color=8}] run setblock ~ ~ ~ oak_sign{Text1: '{"color":"dark_aqua","nbt":"CustomName","entity":"@e[tag=sp_selected]","interpret":true}'}
execute if entity @s[scores={ft_color=9}] run setblock ~ ~ ~ oak_sign{Text1: '{"color":"dark_blue","nbt":"CustomName","entity":"@e[tag=sp_selected]","interpret":true}'}
execute if entity @s[scores={ft_color=10}] run setblock ~ ~ ~ oak_sign{Text1: '{"color":"blue","nbt":"CustomName","entity":"@e[tag=sp_selected]","interpret":true}'}
execute if entity @s[scores={ft_color=11}] run setblock ~ ~ ~ oak_sign{Text1: '{"color":"light_purple","nbt":"CustomName","entity":"@e[tag=sp_selected]","interpret":true}'}
execute if entity @s[scores={ft_color=12}] run setblock ~ ~ ~ oak_sign{Text1: '{"color":"dark_purple","nbt":"CustomName","entity":"@e[tag=sp_selected]","interpret":true}'}
execute if entity @s[scores={ft_color=13}] run setblock ~ ~ ~ oak_sign{Text1: '{"color":"white","nbt":"CustomName","entity":"@e[tag=sp_selected]","interpret":true}'}
execute if entity @s[scores={ft_color=14}] run setblock ~ ~ ~ oak_sign{Text1: '{"color":"gray","nbt":"CustomName","entity":"@e[tag=sp_selected]","interpret":true}'}
execute if entity @s[scores={ft_color=15}] run setblock ~ ~ ~ oak_sign{Text1: '{"color":"dark_gray","nbt":"CustomName","entity":"@e[tag=sp_selected]","interpret":true}'}
execute if entity @s[scores={ft_color=16}] run setblock ~ ~ ~ oak_sign{Text1: '{"color":"black","nbt":"CustomName","entity":"@e[tag=sp_selected]","interpret":true}'}
#endif


# Copy the text of the sign to the armor stand's name
data modify entity @e[type=armor_stand,distance=..3,limit=1,tag=sp_selected] CustomName set from block ~ ~ ~ front_text.messages[0]

# Removes the sign
setblock ~ ~ ~ air

# Sets the armor stand Invisible, Invulnerable and shows its Custom Name. Also removes its gravity
function floating_texts:armor_stands/activate

# Adds the 'ft_text_display' tag so we can know at any time which armor stand was modified by this datapack
tag @e[type=armor_stand,distance=..3,limit=1,sort=nearest,tag=sp_selected] add ft_text_display

# Removes tags and resets scores
tag @e[type=armor_stand,distance=..3,limit=1,sort=nearest,tag=sp_selected] remove sp_selected
scoreboard players set @s ft_color 0
scoreboard players enable @s ft_color