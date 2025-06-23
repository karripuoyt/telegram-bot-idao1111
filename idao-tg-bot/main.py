import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# 🔐 Твой токен (убедись, что он остаётся в секрете)
BOT_TOKEN = "7893976770:AAGW5nwHnKCHVk372V23FKMUInv2QgD_Yuk"

logging.basicConfig(level=logging.INFO)

user_lang = {}

# 📋 Названия кнопок (всего по 8)
menu_buttons = {
    "ru": [
        ("Что такое IDAOℹ️📘?", "what_ru"),
        ("Роли в Discord🎭💬", "roles_ru"),
        ("Для чего создана платформа IDAO Forecasts🎯🧠", "What is the IDAO Forecasts platform for_ru"),
        ("Ресурсы проекта🌐🔗", "resources_ru"),
        ("Турниры и награды🏆💰", "Tournaments and awards_ru"),
        ("Как использовать  IDAO Forecasts🧭📊", "How to use IDAO Forecasts_ru"),
        ("Полезные статьи о проекте📰✨", "Useful articles on the project_ru"),
        ("Обратная связь | задать вопрос ✉️❓", "Feedback | ask a questio_ru"),
    ],
    "en": [
        ("What is IDAOℹ️📘?", "what_en"),
        ("roles in discord🎭💬", "roles_en"),
        ("What is the IDAO Forecasts platform for🎯🧠", "forecast_en"),
        ("Project resources🌐🔗", "resources_en"),
        ("Tournaments and awards🏆💰", "tournaments_en"),
        ("How to use IDAO Forecasts🧭📊", "howtouse_en"),
        ("Useful articles on the project📰✨", "useful_en"),
        ("Feedback | ask a questio ✉️❓", "feedback_en"),
    ]
}

# 📝 Пустые шаблоны текстов
menu_texts = {
    "what_ru": """ 🌍 IDAO: Будущее децентрализованных финансов

IDAO — это не просто проект, а шаг к новой финансовой реальности. Мы создаём платформу, которая заменяет устаревшие модели на прозрачные, безопасные и децентрализованные решения на основе блокчейна.


❓ Что такое IDAO?

IDAO — это инструмент для участия в глобальной децентрализованной экосистеме, где управление и принятие решений больше не зависят от посредников.


🛡 Что мы меняем?

Мы убираем централизацию, делая финансовые инструменты доступными каждому. IDAO разрушает барьеры и предлагает простую, надёжную альтернативу традиционным системам.


💎 Почему децентрализация — это плюс?

— Полная прозрачность действий

— Высокий уровень безопасности

— Низкие издержки и быстрая работа

— Гибкость и открытость к изменения будущего

🔜 Вперёд с IDAO

Мы прокладываем путь к новым финансовым стандартам. Присоединяйся к сообществу IDAO — стань частью децентрализованного будущего!""",
    "roles_ru": """5️⃣ Роли в сообществе IDAO 5️⃣

В Discord-сообществе IDAO каждый участник ценен, а за вклад и активность можно получить уникальные роли, которые подчеркивают вашу значимость и дают возможность участвовать в развитии проекта.

📌 Что означает каждая роль? Давайте разберёмся:

🥇 Pioneer — один из первых 200 участников, кто присоединился к Discord до его публичного запуска и сгенерировал активационные коды.

🔥 Running Hot — за качественные и содержательные посты в чате, которые оживляют общение и несут пользу.

📣 DAOvangelist — присваивается тем, кто делает больше, чем ожидается: помогает развивать проект, проявляет инициативу и продвигает IDAO.

🧠 Quant — для тех, кто делает глубокий аналитический вклад: пишет вдумчивые посты и помогает другим лучше понять проект.

🎨 DAOrist & ViDao — выдаётся за высококлассные арты и видео, посвящённые проекту и его идеям.

🧩 Memelier — новая роль для тех, кто создаёт умные, оригинальные и цепляющие мемы, усиливающие узнаваемость IDAO и вовлечённость сообщества.

🤝 DAOer — для участников, которые активно помогают другим: отвечают на вопросы, направляют новичков и поддерживают позитивную атмосферу.

💎 NadOG — для ветеранов, кто давно в проекте и регулярно вносит ощутимый вклад в развитие IDAO.

💬 Nads — за дружелюбное, осмысленное и активное участие в чате, которое объединяет сообщество.

Эти роли — не просто значки. Это признание вашей активности, вклада и уникальности. Кто бы вы ни были — художник, аналитик, меммейкер или просто отзывчивый участник — у вас есть возможность проявить себя и быть замеченным.

⭐️ Присоединяйтесь к IDAO — создавайте, общайтесь, развивайтесь и вместе с нами стройте децентрализованное будущее! ⭐️""",
    "What is the IDAO Forecasts platform for_ru": """В мире криптовалюты каждый шаг и каждое решение могут стать решающими для вашего финансового успеха. В условиях бурного рынка, где каждый трейдер стремится получить преимущество, IDAO Forecast предоставляет уникальное пространство, которое объединяет трейдеров и новичков для создания наиболее точных и ценных прогнозов. 

🕯 Конкурентная среда для прогнозирования 

IDAO Forecast — это не просто платформа для прогнозов. Это динамичная конкурентная среда, в которой пользователи соревнуются в точности своих предсказаний касательно цен на криптовалюты. Каждый трейдер имеет возможность продемонстрировать свои аналитические способности, а новичкам открывается шанс учиться у лучших и использовать их прогнозы для увеличения своих доходов. 

💡 Монетизация навыков и прозрачность информации 

Трейдеры на IDAO Forecast могут монетизировать свои навыки прогнозирования, получая вознаграждение за точность своих прогнозов. Это создает стимул для улучшения аналитических навыков и предоставления более качественных прогнозов. Для новичков платформа становится ценным источником информации. Прозрачность данных позволяет пользователям видеть прогнозы лучших аналитиков и принимать более обоснованные решения. 

🤝 Объединение трейдеров и новичков 

IDAO Forecast создает уникальное пространство, где трейдеры и новички могут сосуществовать и сотрудничать. Опытные трейдеры делятся своими знаниями, а новички имеют возможность учиться и расти. Это сотрудничество укрепляет сообщество и помогает каждому участнику платформы достигать лучших результатов. 

📊 Коллективная мудрость и ценность прогнозов 

Чем больше пользователей делают прогнозы на IDAO Forecast, тем более ценной становится информация на платформе. Прогнозы широкой аудитории позволяют усреднить результаты и создать более точное представление о рыночных тенденциях. Это, в свою очередь, помогает трейдерам принимать более информированные решения и увеличивать свои вознаграждения. 

🔍 Настроение рынка и усредненные результаты 

IDAO Forecast собирает прогнозы от множества пользователей, что позволяет проанализировать результаты и определить общее настроение рынка. Это мощный инструмент для анализа и предсказания рыночных движений, который дает пользователям уникальные возможности для улучшения своих стратегий торговли. 

6️⃣ Присоединяйтесь к IDAO Forecast 

Если вы стремитесь улучшить свои навыки прогнозирования или хотите использовать знания лучших аналитиков для увеличения своих доходов, IDAO Forecast — это идеальная платформа для вас.""", 
    "resources_ru": """🌐 Полезные ссылки:
• Сайт: https://idao.finance

• Платформа: https://forecast.idao.finance

• Discord: https://discord.gg/idao

• X/Twitter: https://x.com/idaofinance

• IDAO Announcement: https://t.me/IDAOfinance

• IDAO Announcement CIS: https://t.me/IDAO_finance""", 
    "Tournaments and awards_ru": """⭐️ Ежемесячные турниры на IDAO Forecast! ⭐️ 

❓ Что вас ждет? 

1️⃣ Ежемесячные турниры: каждый месяц во время бета-тестирования вы сможете участвовать в конкурсе, набирая поинты за точные прогнозы. 

2️⃣ Призовой фонд: лучшие 20 пользователей, которые набрали больше всего поинтов по итогам месяца разделят между собой 3000 POL! 

3️⃣ Условия участия: нет минимального порога по баллам! Даже если вы получите всего 2 балла и попадете в топ-20 — вас всё равно ждут вознаграждения! 

4️⃣ Максимальные стимулы: мы стремимся создать комфортные и выгодные условия для нашего комьюнити и дать вам возможность начать зарабатывать уже сейчас! 

5️⃣ Прозрачность: в нашем лидерборде на платформе вы сможете фильтровать ежемесячную статистику каждого участника и просматривать её для того, чтобы знать, сколько вам осталось набрать поинтов для попадания в топ-20.  

📊 Вы можете начать прогнозировать и участвовать в соревновании в любое время! Каждый прогноз — это шанс не только улучшить свои навыки, но и получить реальные призы.""", 
    "How to use IDAO Forecasts_ru": """🚀 Как начать работу с платформой IDAO FORECAST:

1️⃣ Перейдите на платформу:
👉 https://forecast.idao.finance/

2️⃣ Подключите кошелёк (рекомендуется MetaMask)

3️⃣ Выберите тип прогноза:
• Краткосрочные
• Среднесрочные
• Долгосрочные
Выберите подходящий именно вам.

4️⃣ Создайте прогноз:
✍️ Введите необходимые параметры и нажмите «Создать прогноз».
⚠️ Для создания прогноза требуется минимальное количество токена POL.

5️⃣ Просмотрите результаты других участников:
📊 Загляните в раздел лидерборда, чтобы увидеть сравнение ваших прогнозов с прогнозами других.

6️⃣ Зарабатывайте поинты:
🏆 Получайте поинты за каждый созданный прогноз. Чем точнее прогнозы — тем больше очков.
💰 В будущем возможны вознаграждения для активных пользователей!

🔹 Обратите внимание, что на платформе доступен также режим Up/Down — быстрые бинарные опционы. 

📈 Вы можете делать прогнозы, будет ли цена выбранного токена (BTC, ETH, BNB, XRP, SOL) выше или ниже через 5 – 15 мин. 
💵 Ставки принимаются в POL и USDT, максимальная ставка — 3 USDT.
📊 Выигрыш — от 1.5x до 1.9x.
⏱️ Таймфреймы — 5 или 15 минут.

Это дополнительный формат для тех, кто предпочитает быстрые решения и мгновенные результаты.

🔗 Начните использовать платформу: https://forecast.idao.finance/""",
    "Useful articles on the project_ru": """• Russian: https://teletype.in/@odyvan52/idao
• English: https://medium.com/@odyvan/idao-forecast-crypto-predictions-with-an-eye-on-the-upcoming-airdrop-ecb28e22b3e6""", 
    "Feedback | ask a questio_ru": "COMMUNITY MANAGER: @IDAO_cm 5️⃣", 
    "what_en": """🌍 IDAO: The Future of Decentralized Finance

IDAO is more than just a project — it's a step toward a new financial reality. We're building a platform that replaces outdated systems with transparent, secure, and decentralized solutions powered by blockchai

❓ What is IDAO?n.11

IDAO is a tool for participating in a global decentralized ecosystem, where decision-making and governance are no longer controlled by intermediaries.

🛡 What are we changing?

We're removing centralization to make financial tools accessible to everyone. IDAO breaks down barriers and offers a simple, reliable alternative to traditional systems.


💎 Why decentralization matters:

— Full transparency of actions

— High level of security

— Low costs and fast operations

— Flexibility and openness to future changes

🔜 Forward with IDAO

We're paving the way toward new financial standards. Join the IDAO community and become part of the decentralized future!""", 
    "roles_en": """5️⃣ Roles in the IDAO Community 5️⃣

In the IDAO Discord community, every member matters. Your contributions can earn you unique roles that recognize your impact and give you a voice in shaping the project’s future.

📌 Let’s break down what each role means:

🥇 Pioneer — awarded to the first 200 members who joined the Discord before it went public and generated activation codes.

🔥 Running Hot — given for high-quality, valuable posts that spark conversation and bring insights to the community.

📣 DAOvangelist — for those who consistently go above and beyond, helping grow the project and spreading its vision.

🧠 Quant — granted to members who provide deep insights and thoughtful content, helping others better understand IDAO.

🎨 DAOrist & ViDao — for those who create high-quality visual content, such as artwork and videos dedicated to IDAO.

🧩 Memelier — a role for creative minds who make clever, original, and engaging memes that help promote IDAO and build community culture.

🤝 DAOer — for members who support others, answer questions, guide newcomers, and keep the community welcoming and helpful.

💎 NadOG — for long-time contributors who’ve shown consistent dedication and support for the project over time.

💬 Nads — awarded for friendly, meaningful, and active participation in the chat that helps strengthen the community vibes. 

These roles are more than just titles — they reflect your value to the community. Whether you're a content creator, helper, meme wizard, or an engaged member, there’s a role for you to shine.

⭐️ Join IDAO, contribute, connect, and help shape the decentralized future with us! ⭐️""", 
    "forecast_en": """In the world of cryptocurrency, every step and every decision can be decisive for your financial success. In a turbulent market where every trader strives to gain an edge, IDAO Forecast provides a unique space that brings together traders and beginners to create the most accurate and valuable forecasts. 

🕯 Competitive forecasting environment 

IDAO Forecast is not just a forecasting platform. It is a dynamic competitive environment where users compete in the accuracy of their cryptocurrency price predictions. Every trader has the opportunity to demonstrate their analytical skills, and beginners have a chance to learn from the best and use their forecasts to increase their income. 

💡 Monetization of skills and transparency of information 

Traders on IDAO Forecast can monetize their forecasting skills by receiving rewards for the accuracy of their forecasts. This creates an incentive to improve analytical skills and provide better forecasts. For beginners, the platform becomes a valuable source of information. Data transparency allows users to see the forecasts of the best analysts and make more informed decisions. 

🤝 Bringing traders and beginners together

IDAO Forecast creates a unique space where traders and beginners can coexist and collaborate. Experienced traders share their knowledge, and beginners have the opportunity to learn and grow. This collaboration strengthens the community and helps each participant on the platform achieve better results.

📊 Collective wisdom and the value of forecasts

The more users make forecasts on IDAO Forecast, the more valuable the information on the platform becomes. Forecasts from a wide audience allow for averaging results and creating a more accurate picture of market trends. This, in turn, helps traders make more informed decisions and increase their rewards.

🔍 Market sentiment and average results

IDAO Forecast collects forecasts from many users, allowing it to analyze the results and determine the overall market sentiment. It is a powerful tool for analyzing and predicting market movements, which gives users unique opportunities to improve their trading strategies.

 6️⃣ Join IDAO Forecast

If you are looking to improve your forecasting skills or want to leverage the knowledge of top analysts to increase your revenue, IDAO Forecast is the perfect platform for you.""",
    "resources_en": """🌐 Useful links:
• Website: https://idao.finance

• Platform: https://forecast.idao.finance

• Discord: https://discord.gg/idao

• X/Twitter: https://x.com/idaofinance

• IDAO Announcement: https://t.me/IDAOfinance

• IDAO Announcement CIS: https://t.me/IDAO_finance""", 
    "tournaments_en": """⭐️ Monthly tournaments on IDAO Forecast! ⭐️ 

❓ What awaits you? 

1️⃣ Monthly tournaments: every month during the beta testing, you will be able to participate in the contest, gaining points for accurate predictions. 

2️⃣ Prize fund: the best 20 users who have accumulated the most points at the end of the month will share 3000 POL among themselves! 

3️⃣ Participation conditions: there is no minimum threshold for points! Even if you get only 2 points and get into the top 20 - rewards are still waiting for you! 

4️⃣ Maximum incentives: we strive to create comfortable and profitable conditions for our community and give you the opportunity to start earning now! 

5️⃣ Transparency: in our leaderboard on the platform, you will be able to filter the monthly statistics of each participant and view it in order to know how many points you have left to get into the top 20. 

📊 You can start predicting and participate in the competition at any time! Each prediction is a chance to not only improve your skills, but also""",
    "howtouse_en": """🚀 How to get started with the IDAO FORECAST platform:

1️⃣ Go to the platform:
👉 https://forecast.idao.finance/

2️⃣ Connect a wallet (MetaMask is recommended)

3️⃣ Select the forecast type:
• Short-term
• Medium-term
• Long-term
Choose the one that suits you.

4️⃣ Create a forecast:
✍️ Enter the required parameters and click "Create forecast".
⚠️ A minimum amount of POL token is required to create a forecast.

5️⃣ View other participants' results:
📊 Check out the leaderboard section to see how your forecasts compare to others.

6️⃣ Earn points:
🏆 Receive points for each forecast you create.  The more accurate the forecasts, the more points.
💰 In the future, rewards for active users are possible!

🔹 Please note that the platform also offers the Up/Down mode — fast binary options.

📈 You can make forecasts on whether the price of the selected token (BTC, ETH, BNB, XRP, SOL) will be higher or lower in 5-15 minutes.

💵 Bets are accepted in POL and USDT, the maximum bet is 3 USDT.
📊 Winnings — from 1.5x to 1.9x.
⏱️ Timeframes — 5 or 15 minutes.

This is an additional format for those who prefer quick decisions and instant results.

🔗 Start using the platform: https://forecast.idao.finance/""", 
    "useful_en": """• Russian: https://teletype.in/@odyvan52/idao
• English: https://medium.com/@odyvan/idao-forecast-crypto-predictions-with-an-eye-on-the-upcoming-airdrop-ecb28e22b3e6""", 
    "feedback_en": "COMMUNITY MANAGER: @IDAO_cm 5️⃣", 
}

# 🔙 Кнопки назад
back_buttons = {
    "ru": InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Назад в меню", callback_data="back_ru")]]),
    "en": InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Back to menu", callback_data="back_en")]])
}


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("🇷🇺 Русский", callback_data="lang_ru"),
            InlineKeyboardButton("🇬🇧 English", callback_data="lang_en")
        ]
    ]
    await update.message.reply_text("🌐 Выберите язык / Choose your language:", reply_markup=InlineKeyboardMarkup(keyboard))


async def handle_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data
    user_id = query.from_user.id

    if data.startswith("lang_"):
        lang = data.split("_")[1]
        user_lang[user_id] = lang
        await send_main_menu(query, lang)

    elif data.startswith("back_"):
        lang = data.split("_")[1]
        await send_main_menu(query, lang)

    else:
        lang = "ru" if "_ru" in data else "en"
        text = menu_texts.get(data, "🔧 Текст пока не задан." if lang == "ru" else "🔧 Content not set yet.")
        await query.edit_message_text(text=text, reply_markup=back_buttons[lang])


async def send_main_menu(query, lang):
    keyboard = [
        [InlineKeyboardButton(text, callback_data=callback)]
        for text, callback in menu_buttons[lang]
    ]
    await query.edit_message_text(
        text="📋 Выберите раздел:" if lang == "ru" else "📋 Choose a section:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


# ▶️ Запуск
app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(handle_callback))

print("✅ Бот запущен")
app.run_polling()
