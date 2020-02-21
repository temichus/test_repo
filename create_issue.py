import asyncio
import os

from aiohttp.client import ClientSession
from octomachinery.github.api.tokens import GitHubOAuthToken
from octomachinery.github.api.raw_client import RawGitHubAPI

async def main():
    access_token = GitHubOAuthToken(os.environ['GITHUB_TOKEN'])
    async with ClientSession() as http_session:
        gh = RawGitHubAPI(
            access_token,
            session=http_session,
            user_agent='temichus',
        )
        # await gh.post(
        #     '/repos/temichus/test_repo/issues',
        #     data={
        #         'title': 'We got a problem',
        #         'body': 'Use more emoji!',
        #     },
        # )
        await gh.patch(
            '/repos/temichus/test_repo/issues{/number}',
            data={'state': 'closed'},
            url_vars={'number': '1'},
        )


asyncio.run(main())