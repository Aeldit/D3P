# D3P (DataPack PreProcessor)

This program takes a Datapack directory as input and for each Minecraft version found
in `.mcfunction` files, a directory with the name of the version will be created.

## Usage

```shell
./d3p.py -d path/to/datapack
```


## Detailed explanation
This directory will contain the same files and folders as the Datapack given as argument, but
the `.mcfunction` files will be preprocessed before.

For example, lets say we have a pack with this tree :

```shell
.
├── data
│   ├── ad
│   │   └── advancements
│   │       └── root.json
│   ├── datapack_name
│   │   ├── functions
│   │   │   └──  .mcfunction
│   └── minecraft
│       └── tags
│           └── functions
│               └── load.json
├── pack.mcmeta
└── pack.png
```

And the file ` .mcfunction` contains this:

```mcfunction
# Sets the color on the sign's text
#ver=1.20.x
execute if entity @s[scores={ft_color=1}] run setblock ~ ~ ~ oak_sign{front_text: {messages: ['{"color":"dark_red","nbt":"CustomName","entity":"@e[tag=sp_selected]","interpret":true}', '{"text":""}', '{"text":""}', '{"text":""}']}}
execute if entity @s[scores={ft_color=2}] run setblock ~ ~ ~ oak_sign{front_text: {messages: ['{"color":"red","nbt":"CustomName","entity":"@e[tag=sp_selected]","interpret":true}', '{"text":""}', '{"text":""}', '{"text":""}']}}
execute if entity @s[scores={ft_color=3}] run setblock ~ ~ ~ oak_sign{front_text: {messages: ['{"color":"gold","nbt":"CustomName","entity":"@e[tag=sp_selected]","interpret":true}', '{"text":""}', '{"text":""}', '{"text":""}']}}
#ver=1.19.4
execute if entity @s[scores={ft_color=1}] run setblock ~ ~ ~ oak_sign{Text1: '{"color":"dark_red","nbt":"CustomName","entity":"@e[tag=sp_selected]","interpret":true}'}
execute if entity @s[scores={ft_color=2}] run setblock ~ ~ ~ oak_sign{Text1: '{"color":"red","nbt":"CustomName","entity":"@e[tag=sp_selected]","interpret":true}'}
execute if entity @s[scores={ft_color=3}] run setblock ~ ~ ~ oak_sign{Text1: '{"color":"gold","nbt":"CustomName","entity":"@e[tag=sp_selected]","interpret":true}'}
#endver

# Copy the text of the sign to the armor stand's name
data modify entity @e[type=armor_stand,distance=..3,limit=1,tag=sp_selected] CustomName set from block ~ ~ ~ front_text.messages[0]

# Removes the sign
setblock ~ ~ ~ air
```

We have 2 versions ; `1.20.x` and `1.19.4` ; which means that 2 directories will be created

We will then have this tree:

```shell
.
├── 1.20.x
│   ├── data
│   │   ├── ad
│   │   │   └── advancements
│   │   │       └── root.json
│   │   ├── datapack_name
│   │   │   ├── functions
│   │   │   │   └──  test.mcfunction
│   │   └── minecraft
│   │       └── tags
│   │           └── functions
│   │               └── load.json
│   ├── pack.mcmeta
│   └── pack.png
└── 1.19.4
    ├── data
    │   ├── ad
    │   │   └── advancements
    │   │       └── root.json
    │   ├── datapack_name
    │   │   ├── functions
    │   │   │   └──  test.mcfunction
    │   └── minecraft
    │       └── tags
    │           └── functions
    │               └── load.json
    ├── pack.mcmeta
    └── pack.png
```

However, `1.20.x/data/datapack_name/functions/test.mcfunction` and
`1.19.4/data/datapack_name/functions/test.mcfunction` will not have the same contents:

For `1.20.x`:
```mcfunction
# Sets the color on the sign's text
execute if entity @s[scores={ft_color=1}] run setblock ~ ~ ~ oak_sign{front_text: {messages: ['{"color":"dark_red","nbt":"CustomName","entity":"@e[tag=sp_selected]","interpret":true}', '{"text":""}', '{"text":""}', '{"text":""}']}}
execute if entity @s[scores={ft_color=2}] run setblock ~ ~ ~ oak_sign{front_text: {messages: ['{"color":"red","nbt":"CustomName","entity":"@e[tag=sp_selected]","interpret":true}', '{"text":""}', '{"text":""}', '{"text":""}']}}
execute if entity @s[scores={ft_color=3}] run setblock ~ ~ ~ oak_sign{front_text: {messages: ['{"color":"gold","nbt":"CustomName","entity":"@e[tag=sp_selected]","interpret":true}', '{"text":""}', '{"text":""}', '{"text":""}']}}

# Copy the text of the sign to the armor stand's name
data modify entity @e[type=armor_stand,distance=..3,limit=1,tag=sp_selected] CustomName set from block ~ ~ ~ front_text.messages[0]

# Removes the sign
setblock ~ ~ ~ air
```

For `1.19.4`:

```mcfunction
# Sets the color on the sign's text
execute if entity @s[scores={ft_color=1}] run setblock ~ ~ ~ oak_sign{Text1: '{"color":"dark_red","nbt":"CustomName","entity":"@e[tag=sp_selected]","interpret":true}'}
execute if entity @s[scores={ft_color=2}] run setblock ~ ~ ~ oak_sign{Text1: '{"color":"red","nbt":"CustomName","entity":"@e[tag=sp_selected]","interpret":true}'}
execute if entity @s[scores={ft_color=3}] run setblock ~ ~ ~ oak_sign{Text1: '{"color":"gold","nbt":"CustomName","entity":"@e[tag=sp_selected]","interpret":true}'}

# Copy the text of the sign to the armor stand's name
data modify entity @e[type=armor_stand,distance=..3,limit=1,tag=sp_selected] CustomName set from block ~ ~ ~ front_text.messages[0]

# Removes the sign
setblock ~ ~ ~ air
```

