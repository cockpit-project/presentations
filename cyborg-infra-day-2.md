---
title: How we hack on Cockpit Infrastructure
subtitle:
author:
 - Martin Pitt, Sanne Raymaekers
email: mpitt@redhat.com, sraymaek@redhat.com
theme: Singapore
header-includes:
 - \setbeameroption{show notes}
...

# Goal

infrastructure ~ code

PR → container rebuilds, private temp deployment, validate against product main branches

land PR → redeploy to production

:::notes
- most of us have become really good at self-validating changes to our product code with test gating
- ideal: want to treat changes to infrastructure alike: submit a PR, builds changed container images
- in Cockpit team we are far from that
- takes a lot of learning of new concepts and infrastructure, needs to offset the cost of classic deploy-watch-rollback
:::
