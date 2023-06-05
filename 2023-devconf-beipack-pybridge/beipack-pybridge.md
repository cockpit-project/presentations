---
title: Monty Python's Flying Cockpit
subtitle: devconf.cz 2023
author:
 - Allison Karlitskaya, Martin Pitt
email: allison.karlitskaya@redhat.com, mpitt@redhat.com
theme: Singapore
header-includes:
 - \hypersetup{colorlinks=true}
 - \setbeameroption{hide notes}
...

# Cockpit intro

- Interactive Server admin web interface
- Setup and troubleshooting for one or a few machines

:::notes
- For this talk we assume a basic familiarity with Cockpit
- If you have never seen it, the short-short version. We'll also do demos
- Conceptually: Linux session running in a web browser; moral server equivalent of what GNOME is on a desktop
- Tool for experimenting, learning, troubleshooting, and doing infrequent tasks
:::

# Architecture

![high-level architecture](./cockpit-system-apis.png) \

:::notes
- To understand this talk, you need to know a bit about how cockpit works internally
- Consider what happens with normal SSH session: You want to do stuff on a
  remote OS which requires running commands, opening files, perhaps talking
  to a TCP port, and so on. But all that SSH gives you is a text stdin and
  stdout, i.e. a pipe pair.
- What you need to connect these is something that translates
  between that pipe and the executables, sockets, D-Bus interfaces of the OS.
  That is a shell like "bash" for an interactive SSH session.
- Cockpit is a web UI written in JavaScript, but it's the same situation: The
  browser possibly runs on the other side of the planet, and it
  can only talk "websocket", which is essentially a pipe. For cockpit,
  the translator is the bridge. It translates these OS interfaces to a
  multiplexed JSON stream.
:::

# Demo: Current cockpit

TODO: flesh out

:::notes
- Connect to fedsrv with client, explain Client flatpak and cockpit UI
- Show installed cockpit rpms on fedsrv
- Run cockpit-bridge command line for running date and read a file
- Connect to "fresh cloud instance" c9s, get "no bridge found", sob
:::

# Making the bridge portable

 - Be like Ansible: SSH + Python
 - Cloud instances, production machines

TODO: flesh out

:::notes
- TODO: explain; goals, Python
- transition to Lis: to do this, we need a couple of technologies to pull this off
:::

# TODO Lis part: beipack, ferny, etc.

# Demo: Portable bridge

TODO: flesh out

:::notes
- Remember that c2 machine? Let's start our alpha version of cockpit's flatpak with the Python bridge
- Connect to c2, watch jaws drop
:::

# Rollout plan

TODO

# Q & A

Contact:

- `#cockpit` on Fedora Matrix
- https://cockpit-project.org

:::notes
- Home page leads to mailing lists, chat, documentation
- thanks for your attention; Q+A
:::
