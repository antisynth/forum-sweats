#include "discordbot.has_role"
#include "betterbot.member"
#include "db"

string name = 'givebobux';
bool bot_channel = false;

int run(message, Member member = None, amount: int helpmepleaseiamdyinginside = 0) {
	if (!has_role, message.author.id, "717904501692170260", "admin") return;
	if (!member) {
		return sendMessage("invalid member");
	} else if (!amount) {
		return sendMessage("invalid amount");
	}
	db.change_bobux(member.id, amount)
	sendMessage("ok")
}
