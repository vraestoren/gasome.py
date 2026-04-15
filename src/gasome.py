from requests import Session

class Gasome:
	def __init__(self) -> None:
		self.api = "https://api.gasome.com"
		self.session = Session()
		self.session.headers = {"user-agent": "Android"}

	def _post(self, endpoint: str, data: dict = None) -> dict:
		return self.session.post(
			f"{self.api}{endpoint}", data=data).json()

	def _get(self, endpoint: str, params: dict = None) -> dict:
		return self.session.get(
			f"{self.api}{endpoint}", params=params or {}).json()

	def login(self, username: str, password: str) -> dict:
		data = {
			"password": password,
			"username": username
		}
		response = self._post("/v1_2/newLogin", data)
		if "token" in response["data"]:
			self.access_token = response["data"]["token"]
			self.session.headers["authorization"] = f"Bearer {
				self.access_token}"
			self.user_id = self.get_current_user()["data"]["id"]
		return response

	def sign_up(
			self,
			email: str,
			name: str,
			password: str,
			username: str) -> dict:
		data = {
			"email": email,
			"name": name,
			"password": password,
			"username": username
		}
		return self._post("/v1_2/users/signup", data)

	def get_current_user(self) -> dict:
		return self._get("/v1_2/user")

	def get_posts(
			self,
			page: int = 1,
			is_global: bool = False) -> dict:
		params = {
			"page": page,
			"global": is_global
		}
		return self._get("/v1_2/getPosts", params)

	def get_notifications(self, page: int = 1) -> dict:
		params = {"page": page}
		return self._get("/v1_2/notifications", params)

	def get_trends(self) -> dict:
		return self._get("/v1_2/getTrends")

	def get_message_box(self, page: int = 1) -> dict:
		params = {"page": page}
		return self._get("/v1_2/messagebox", params)

	def get_platforms(self) -> dict:
		return self._get("/v1_2/getPlatforms")

	def get_recommended_users(self) -> dict:
		return self._get("/v1_2/recommendedUsers")

	def get_user_info(self, username: str) -> dict:
		params = {"selected_user": username}
		return self._get("/v1_2/info", params)

	def follow_user(self, username: str) -> dict:
		data = {"selected_user": username}
		return self._post("/v1_2/follow", data)

	def unfollow_user(self, username: str) -> dict:
		data = {"selected_user": username}
		return self._post("/v1_2/follow", data)

	def get_user_played(
			self, user_id: int, page: int = 1) -> dict:
		params = {
			"userId": user_id,
			"page": page
		}
		return self._get("/v1_2/played", params)

	def get_user_posts(
			self, user_id: int, page: int = 1) -> dict:
		params = {
			"userId": user_id,
			"page": page
		}
		return self._get("/v1_2/getPostsByUser", params)

	def get_user_old_streams(self, user_id: int) -> dict:
		params = {"userId": user_id}
		return self._get("/v1_2/oldStreams", params)

	def get_user_followers(
			self,
			user_id: int,
			page: int = 1) -> dict:
		params = {
			"userId": user_id,
			"page": page
		}
		return self._get("/v1_2/getFollowers", params)

	def get_user_followings(
			self,
			user_id: int,
			page: int = 1) -> dict:
		params = {
			"userId": user_id,
			"page": page
		}
		return self._get("/v1_2/getFollowing", params)

	def send_message(
			self,
			user_id: str,
			text: str) -> dict:
		data = {
			"contact_id": user_id,
			"text": text
		}
		return self._post("/v1_2/conversation/send", data)

	def create_post(self, text: str) -> dict:
		data = {"text": text}
		return self._post("/v1_2/newPost", data)

	def edit_profile(
			self,
			name: str = None,
			username: str = None,
			bio: str = None,
			email: str = None,
			website: str = None) -> dict:
		data = {
			"name": name,
			"username": username,
			"bio": bio,
			"email": email,
			"website": website
		}
		filtered_data = {
			key: value for key, value in data.items() if value is not None
		}
		return self._post(
			"/v1_2/postUpdateProfile", filtered_data)

	def change_password(
			self,
			old_password: str,
			new_password: str) -> dict:
		data = {
			"newPassword": new_password,
			"password": old_password
		}
		return self._post(
			"/v1_2/updatePassword", data)

	def get_blocked_users(self) -> dict:
		return self._get("/v1_2/blockedUsers")

	def get_conversation(self, user_id: str) -> dict:
		params = {
			"userId": user_id
		}
		return self._get("/v1_2/conversation/", params)

	def search_user(self, query: str) -> dict:
		params = {"search": query}
		return self._get("/v1_2/getSearchUser", params)

	def search_tag(self, query: str) -> dict:
		params = {"search": query}
		return self._get("/v1_2/getSearchTag", params)

	def search_game(self, query: str) -> dict:
		params = {"search": query}
		return self._get("/v1_2/getSearchGame", params)

	def get_post_info(self, post_id: int) -> dict:
		params = {"postId": post_id}
		return self._get("v1_2/getPostById", params)

	def like_post(self, post_id: int) -> dict:
		data = {"postId": post_id}
		return self._post("/v1_2/postLike", data)

	def unlike_post(self, post_id: int) -> dict:
		data = {"postId": post_id}
		return self._post("/v1_2/postLike", data)

	def delete_post(self, post_id: int) -> dict:
		data = {"postId": post_id}
		return self._post("/v1_2/deletePost", data)

	def send_report(
			self,
			type: str,
			post_id: int = None,
			user_id: int = None) -> dict:
		data = {
			"type": type
		}
		if type == "user":
			data["userId"] = user_id
		elif type == "post":
			data["postId"] = post_id
		return self._post("/v1_2/postReport", data)

	def get_trend_topics(self, weekly: bool = False) -> dict:
		params = {"weekly": weekly}
		return self._get(
			"/v1_2/getTrendTopics", params)

	def get_streams(self) -> dict:
		return self._get("/v1_2/streams")

	def delete_stream(self, stream_id: int) -> dict:
		data = {"id": stream_id}
		return self._post("/v1_2/deleteStream", data)

	def get_twitch_user(self, twitch_user_id: str) -> dict:
		params = {"userId": twitch_user_id}
		return self._get("/v1_2/getTwitchUser", params)

	def get_live_stream(self, twitch_user_id: str) -> dict:
		return self._get("/v1_2/getLiveStream", params)

	def block_user(
			self,
			user_id: int = None,
			username: str = None) -> dict:
		data = {}
		if user_id:
			data["userId"] = user_id
		elif username:
			data["username"] = username
		return self._post("/v1_2/block", data)

	def unblock_user(
			self,
			user_id: int = None,
			username: str = None) -> dict:
		data = {}
		if user_id:
			data["userId"] = user_id
		elif username:
			data["username"] = username
		return self._post("/v1_2/unblock", data)
