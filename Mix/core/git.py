#
# Copyright (C) 2023-2024 by YukkiOwner@Github, < https://github.com/YukkiOwner >.
#
# This file is part of < https://github.com/YukkiOwner/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/YukkiOwner/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.
#

import asyncio
import shlex
from typing import Tuple

from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError
from team.nandev.class_log import LOGGER

import config


def install_req(cmd: str) -> Tuple[str, str, int, int]:
    async def install_requirements():
        args = shlex.split(cmd)
        process = await asyncio.create_subprocess_exec(
            *args,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        return (
            stdout.decode("utf-8", "replace").strip(),
            stderr.decode("utf-8", "replace").strip(),
            process.returncode,
            process.pid,
        )

    return asyncio.get_event_loop().run_until_complete(install_requirements())


def git():
    REPO_LINK = config.upstream_repo
    if config.git_token:
        GIT_USERNAME = REPO_LINK.split("com/")[1].split("/")[0]
        TEMP_REPO = REPO_LINK.split("https://")[1]
        UPSTREAM_REPO = f"https://{GIT_USERNAME}:{config.git_token}@{TEMP_REPO}"
    else:
        UPSTREAM_REPO = config.upstream_repo

    try:
        repo = Repo()  # Mendeteksi repository di direktori saat ini
        LOGGER.info("Git repository found.")
    except InvalidGitRepositoryError:
        LOGGER.warning("No valid Git repository found. Initializing...")
        repo = Repo.init("/app")  # Inisialisasi repository di direktori /app
        origin = repo.create_remote("origin", UPSTREAM_REPO)
        origin.fetch()
        repo.create_head(config.upstream_branch, origin.refs[config.upstream_branch])
        repo.heads[config.upstream_branch].set_tracking_branch(origin.refs[config.upstream_branch])
        repo.heads[config.upstream_branch].checkout()
    except GitCommandError as e:
        LOGGER.error(f"Git command error: {e}")
        return

    try:
        origin = repo.remote("origin")
        origin.pull(config.upstream_branch)
        LOGGER.info(f"Fetched updates from: {UPSTREAM_REPO}")
    except GitCommandError as e:
        LOGGER.error(f"Failed to fetch updates: {e}")
        repo.git.reset("--hard", "FETCH_HEAD")
