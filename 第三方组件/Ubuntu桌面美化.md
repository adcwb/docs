ubuntu桌面美化



Dash to Dock安装

```
Firefox--> 扩展--> GNOME Shell integration --> Dash to Dock
```



Conky桌面监控组件

```shell
sudo apt-get install conky conky-all

vim ~/.conkyrc
-- vim: ts=4 sw=4 noet ai cindent syntax=lua
--[[
Conky, a system monitor, based on torsmo

Any original torsmo code is licensed under the BSD license

All code written since the fork of torsmo is licensed under the GPL

Please see COPYING for details

Copyright (c) 2004, Hannu Saransaari and Lauri Hakkarainen
Copyright (c) 2005-2012 Brenden Matthews, Philip Kovacs, et. al. (see AUTHORS)
All rights reserved.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
]]

conky.config = {
    alignment = 'top_right',
    background = true,
    border_width = 1,
    cpu_avg_samples = 2,
	default_color = 'white',
    default_outline_color = 'white',
    default_shade_color = 'white',
    draw_borders = false,
    draw_graph_borders = true,
    draw_outline = false,
    draw_shades = false,
    use_xft = true,
    font = 'simsunb:size=12',
    gap_x = 5,
    gap_y = 60,
    minimum_height = 5,
	minimum_width = 5,
    net_avg_samples = 2,
    no_buffers = true,
    out_to_console = false,
    out_to_stderr = false,
    extra_newline = false,
    own_window = true,
    own_window_class = 'Conky',
    own_window_type = 'desktop',
    stippled_borders = 0,
    update_interval = 1.0,
    uppercase = false,
    use_spacer = 'none',
    show_graph_scale = false,
    show_graph_range = false,
    own_window_argb_visual = true,
    own_window_argb_value = 50,
    double_buffer = true,
}

conky.text = [[
${scroll 16 $nodename - $sysname $kernel on $machine | }
$hr
${color CDE0E7}$alignc${font FreeMono:pixelsize=70}${time %H:%M}${font}
$alignc${font FreeMono}${color white}${time %Y}-${time  %m}-${time %d}${font}
$hr
${color grey}系统运行时间:$color $uptime
${color grey}CPU当前频率 (in MHz):$color $freq
#${color grey}CPU当前频率 (in GHz):$color $freq_g
${color grey}CPU 使用情况:$color $cpu% ${cpubar 4}
	${color}Processes:$color $processes  ${color}Running:$color $running_processes
${color grey}RAM 使用情况:
	$color $mem/$memmax - $memperc% ${membar 4}
${color grey}Swap 使用情况:
	$color $swap/$swapmax - $swapperc% ${swapbar 4}
${color grey}GPU:
 	${color1}GPU 频率: $alignr ${color}${font}${nvidia gpufreq} Mhz${voffset 3}
 	${color1}Memory 频率: $alignr ${color}${font}${nvidia memfreq} Mhz${voffset 3}
 	${color1}当前温度: $alignr ${color}${font}${nvidia temp}°C ${voffset 3}
$hr
${color grey}文件系统:
    / $color${fs_used /}/${fs_size /} ${fs_bar 6 /}
    /data $color${fs_used /data}/${fs_size /data} ${fs_bar 6 /data}
$hr
${color grey}磁盘 I/O:${color}${font} ${alignr}$diskio
    ${color}读取: ${color}${font} ${goto 80}${color4}${diskiograph_read  15,210 ADFF2F 32CD32 750}${color}
    ${color}写入: ${color}${font} ${goto 80}${color4}${diskiograph_write 15,210 FF0000 8B0000 750}${color}
$hr
${color grey}网卡速率:
    ${color}有线网卡: Up:$color ${upspeed enp7s0} ${color} - Down:$color ${downspeed enp7s0}
    ${color}无线网卡: Up:$color ${upspeed wlp4s0} ${color} - Down:$color ${downspeed wlp4s0}
$hr
${color grey}进程监控:
    ${color}Name              PID   CPU   MEM
    ${color} ${top name 1} ${top pid 1} ${top cpu 1} ${top mem 1}
    ${color} ${top name 2} ${top pid 2} ${top cpu 2} ${top mem 2}
    ${color} ${top name 3} ${top pid 3} ${top cpu 3} ${top mem 3}
    ${color} ${top name 4} ${top pid 4} ${top cpu 4} ${top mem 4}
    ${color} ${top name 5} ${top pid 5} ${top cpu 5} ${top mem 5}
]]


```

