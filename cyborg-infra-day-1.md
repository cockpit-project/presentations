---
title: Cockpit Infrastructure
subtitle:
author:
 - Martin Pitt, Sanne Raymaekers
email: mpitt@redhat.com, sraymaek@redhat.com
theme: Singapore
header-includes:
 - \setbeameroption{hide notes}
...

# Cockpit Team

![screenshot](./cockpit-storage.png)\ 

- Interactive Server admin web interface
- Included in all major distros, uses over 100 OS APIs
- 7 team members
- Automated tests, releases, npm/translation updates, VM/container image refreshes

:::notes
- Conceptually: Linux session running in a web browser; moral equivalent of what GNOME is on a desktop
- talks to > 100 system APIs, times > 10 supported releases → moving target, things break all the time
- small team, heavily dependent on infrastructure
- automated testing, releasing, code hygiene, updating VM and container images
:::

# Our Automation Principles

\qquad \qquad \qquad \qquad ![container](./container.pdf){width=12%} \qquad \qquad ![no magic infra](./no-magic.pdf){width=12%}\ 

Containerize everything → simple and safe to run locally

No magic infrastructure → reproducible, cloud portability

Automated deployment → scalable, recoverable, ~~bus factor 1~~

:::notes
- Formula: Containerize everything plus no magic infrastructure
- Humans first: Make it simple and enjoyable to locally hack on tests, automation, CI
- Containers are easy to reproduce, easy to run locally and on different cloud platforms
- CI/CD uses the exact same containers and commands, just more powerful
- Deployed using publicly available ansible scripts (credentials of course are not public :D)
:::

<!-- TODO maybe pull this slide out in to two? One that says which infra we use, and another which details what we run on each ? -->
# Which infrastructure exactly?

- GitHub workflows for all tasks except testing
- CentOS CI openshift cluster
- e2e cluster, system template units
- AWS

:::notes
- GitHub's infra is unlimited, free, zero admin cost, high-level SPOF (if GH goes down we have no project anyway)
- To run tests we need kvm access and internal network access depending on the
  image, so those are not done by GitHub infrastructure
- CentOS CI ocp: powerful, free, no internal tests; replication controllers on multiple nodes
- e2e cluster:
  - very powerful but (increasingly) difficult to maintain (rhel 7 → rhel 8)
  - able to run internal tests
  - hosts image server
  - systemd autorestart controlled docker instance; 10 nodes
- AWS:
  - image server backup in case e2e goes down
  - logging sink
  - tests fallback
  - fully automated using ansible, but pricey
- Always prospecting for new infrastructure :)
:::

<!-- TODO Not sure i got the image conversion right -->
# ![event flow](event-flow.pdf)

:::notes
- webhook → AMQP: webhook is just single instance, but auto-recovers through cold PR/issue scanning (github is single source of truth)
- SPOF: centosci for the webhook/amqp
- weak:
  - test logs (just on one server per cloud)
  - detection/prevention/infra logging (journal/k8s), but has not been a big enough pain point in part due to reproducibility of queue state
  - no metrics, little alerting (email on bots crash)
- strong:
  - mentioned reproducibility and portability
  - platform agnostic work queue
  - deployment with public ansible scripts (not 100% automated because imo that would be github PR merge -> deploy main branch)
:::

# Challenges
- test logging and artifacts
- maintaining e2e machines
- hard to find public infra with /dev/kvm

:::notes
- our test logging/artifact infra is very arcane, not portable, too much logic; want to move to standard infra (http post, loki, etc.)
- e2e machines are ever more difficult to keep running; need well-maintained internal infra
- hard to find public infra with /dev/kvm: Travis for a while, but they stopped having free plans
:::
