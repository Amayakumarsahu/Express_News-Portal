"""Seed the database with sample Mumbai news articles."""
from app import app, db
from models import Article, User
from datetime import datetime, timedelta
import random

SAMPLE_ARTICLES = [
    {
        "title": "Mumbai Metro Line 3 Set to Open by June 2026, Promises to Transform City Commute",
        "short_description": "The much-awaited Aqua Line connecting Colaba to SEEPZ will finally begin commercial operations, reducing travel time across the city by up to 40%.",
        "content": """<p>Mumbai's long-awaited Metro Line 3, also known as the Aqua Line, is on track to begin commercial operations by June 2026, according to senior officials of the Mumbai Metro Rail Corporation (MMRC).</p>
<p>The 33.5-kilometer underground corridor connecting Colaba in South Mumbai to SEEPZ in Andheri will feature 27 stations, making it one of the most ambitious urban transit projects in India.</p>
<p>"We have completed over 97% of the civil work and are currently in the testing and commissioning phase," said an MMRC spokesperson. "Trial runs have been successful, and we are confident of meeting the June deadline."</p>
<p>The line is expected to carry approximately 17 lakh passengers daily once fully operational, significantly reducing the burden on Mumbai's overcrowded suburban railway network.</p>
<p>Key stations include Cuffe Parade, Vidhan Bhavan, Churchgate, Mumbai Central, Worli, Bandra-Kurla Complex, and the international airport terminal. The line will also feature interchange facilities with the existing Western and Central railway lines.</p>
<p>Urban planning experts believe the new metro line will not only ease commute times but also boost real estate values along the corridor and promote transit-oriented development in the city.</p>""",
        "category": "Mumbai",
        "author": "Rajesh Sharma",
        "image_url": "/static/images/news-1.jpg",
        "is_featured": True,
        "is_breaking": True,
        "views": 15420
    },
    {
        "title": "BMC Launches ₹2,800 Crore Coastal Road Phase 2 — Bandra to Versova Stretch Approved",
        "short_description": "The second phase of Mumbai's ambitious coastal road project gets green light, promising seamless connectivity along the western seafront.",
        "content": """<p>The Brihanmumbai Municipal Corporation (BMC) has officially approved the second phase of the Mumbai Coastal Road project, covering the stretch from Bandra to Versova at an estimated cost of ₹2,800 crore.</p>
<p>This extension will add approximately 9.5 kilometers to the existing coastal road infrastructure, which currently connects Marine Drive to the Bandra-Worli Sea Link.</p>
<p>"The Phase 2 alignment has been finalized after extensive environmental impact assessments and public consultations," said the Municipal Commissioner. "We expect the project to be completed within 36 months."</p>
<p>The new stretch will feature twin tunnels, elevated sections, and multiple entry/exit ramps. It will also include dedicated cycling tracks and pedestrian walkways along the seafront.</p>
<p>Environmental groups have raised concerns about the impact on marine ecosystems, but BMC officials say comprehensive mitigation measures are in place.</p>""",
        "category": "Mumbai",
        "author": "Priya Deshmukh",
        "image_url": "/static/images/news-2.jpg",
        "is_featured": False,
        "is_breaking": True,
        "views": 12300
    },
    {
        "title": "Maharashtra Government Announces Free Wi-Fi at All Railway Stations Across Mumbai",
        "short_description": "In a digital push, the state government partners with tech companies to provide free high-speed internet at over 120 suburban railway stations.",
        "content": """<p>The Maharashtra government announced a major digital infrastructure initiative on Wednesday, promising free high-speed Wi-Fi connectivity at all 120+ suburban railway stations across the Mumbai Metropolitan Region.</p>
<p>The initiative, launched in partnership with leading telecom providers, will offer passengers up to 1 GB of free daily data at speeds of up to 100 Mbps.</p>
<p>"This is part of our vision to make Mumbai a truly smart city," said the Chief Minister at the launch event at CSMT. "Millions of commuters will now have access to high-speed internet during their daily travels."</p>
<p>The rollout will begin with major stations like CSMT, Dadar, Andheri, Thane, and Borivali, with complete coverage expected by December 2026.</p>""",
        "category": "Technology",
        "author": "Ankit Patel",
        "image_url": "/static/images/news-3.jpg",
        "is_featured": False,
        "is_breaking": False,
        "views": 8900
    },
    {
        "title": "Record Monsoon Preparation: BMC Deploys AI-Powered Flood Prediction System",
        "short_description": "Mumbai's civic body introduces artificial intelligence to predict waterlogging and floods 48 hours in advance, a first for any Indian city.",
        "content": """<p>In a groundbreaking move to combat Mumbai's perennial monsoon flooding, the BMC has deployed an AI-powered flood prediction and early warning system that can forecast waterlogging up to 48 hours in advance.</p>
<p>The system uses real-time data from over 500 IoT sensors installed across the city's drainage network, combined with satellite imagery, weather forecasts, and historical flooding patterns.</p>
<p>"We have trained the AI model on 15 years of monsoon data," explained the head of the BMC's Storm Water Drains department. "The system can predict with 85% accuracy which areas will experience waterlogging during heavy rainfall."</p>
<p>Residents will receive alerts via a dedicated mobile app and SMS notifications, allowing them to plan their commutes and take precautionary measures.</p>
<p>The ₹45-crore project is part of the BMC's broader Smart Mumbai initiative and has been developed in collaboration with IIT Bombay.</p>""",
        "category": "Technology",
        "author": "Meera Iyer",
        "image_url": "/static/images/news-4.jpg",
        "is_featured": False,
        "is_breaking": False,
        "views": 7650
    },
    {
        "title": "Sensex Crosses 95,000 Mark for First Time as Mumbai Markets Rally on Global Cues",
        "short_description": "The BSE benchmark index hit an all-time high, driven by strong FII inflows and positive global sentiment after US Fed signals rate cut.",
        "content": """<p>The BSE Sensex breached the historic 95,000 mark for the first time on Wednesday, driven by robust foreign institutional investor (FII) inflows and positive cues from global markets.</p>
<p>The 30-share benchmark index closed at 95,234.67, up 1,287 points or 1.37% from the previous close. The broader Nifty 50 also hit a new high, closing above 28,900.</p>
<p>Banking, IT, and infrastructure stocks led the rally, with HDFC Bank, TCS, and L&T among the top gainers. The total market capitalization of BSE-listed companies crossed ₹500 lakh crore for the first time.</p>
<p>"The combination of strong domestic fundamentals, expected rate cuts, and resilient corporate earnings is driving the market to new highs," said a senior market analyst at a leading brokerage firm.</p>""",
        "category": "Business",
        "author": "Vikram Shah",
        "image_url": "/static/images/news-5.jpg",
        "is_featured": False,
        "is_breaking": True,
        "views": 18200
    },
    {
        "title": "IPL 2026: Mumbai Indians Seal Playoff Berth with Thrilling Super Over Victory",
        "short_description": "Rohit Sharma's heroic 89 off 48 balls takes Mumbai Indians to a dramatic super over win against Chennai Super Kings at Wankhede Stadium.",
        "content": """<p>Mumbai Indians secured their spot in the IPL 2026 playoffs with a heart-stopping super over victory against Chennai Super Kings at the iconic Wankhede Stadium on Tuesday night.</p>
<p>Captain Rohit Sharma played a magnificent innings of 89 off 48 balls, hitting 7 sixes and 6 fours, to drag Mumbai Indians back from what seemed like a hopeless position.</p>
<p>Chasing 198, Mumbai Indians were reduced to 112/6 in the 14th over before Sharma's counterattack brought them level at 197 in the final ball of the last over.</p>
<p>In the super over, Jasprit Bumrah bowled a masterful over, conceding just 4 runs, before Sharma hit the winning boundary off the second ball to seal a famous victory for the home team.</p>
<p>The win takes Mumbai Indians to 16 points and guarantees them a top-4 finish in the league stage.</p>""",
        "category": "Sports",
        "author": "Sunil Nair",
        "image_url": "/static/images/news-6.jpg",
        "is_featured": False,
        "is_breaking": False,
        "views": 25600
    },
    {
        "title": "Bollywood Star Shah Rukh Khan Inaugurates New Film City Complex in Navi Mumbai",
        "short_description": "The state-of-the-art ₹1,500 crore film production facility promises to put Mumbai back at the center of Indian entertainment industry.",
        "content": """<p>Bollywood superstar Shah Rukh Khan inaugurated the new Navi Mumbai Film City on Wednesday, a sprawling 100-acre state-of-the-art production facility that aims to rival Hollywood's best studios.</p>
<p>The ₹1,500 crore complex features 15 sound stages, underwater shooting tanks, virtual production studios with LED walls, post-production suites, and accommodation for cast and crew.</p>
<p>"Mumbai has always been the heart of Indian cinema, and this facility ensures it stays that way for the next century," Khan said at the inauguration ceremony.</p>
<p>The facility, developed by the Maharashtra Film, Stage and Cultural Development Corporation, is expected to generate over 10,000 direct and indirect jobs in the region.</p>""",
        "category": "Entertainment",
        "author": "Fatima Khan",
        "image_url": "/static/images/news-7.jpg",
        "is_featured": False,
        "is_breaking": False,
        "views": 19800
    },
    {
        "title": "Mumbai's Air Quality Improves to 'Good' Category for First Time in March",
        "short_description": "Thanks to stricter emission norms and increased green cover, Mumbai's AQI drops to 45, the best reading in a decade for the month of March.",
        "content": """<p>Mumbai recorded its best air quality in over a decade for the month of March, with the Air Quality Index (AQI) dropping to 45 — firmly in the 'Good' category — according to data from the System of Air Quality and Weather Forecasting And Research (SAFAR).</p>
<p>Experts attribute the improvement to a combination of factors including stricter vehicle emission norms (BS-VI compliance), the expansion of the metro network reducing vehicular traffic, increased green cover from the BMC's tree plantation drive, and favorable wind patterns.</p>
<p>"This is a significant achievement for a city that has traditionally struggled with air pollution," said an environmental scientist at IIT Bombay.</p>
<p>The BMC's ambitious plan to create 50 new urban forests under the Miyawaki method has also contributed to the improvement, with over 2 lakh trees planted in the last two years.</p>""",
        "category": "Mumbai",
        "author": "Kavita Rao",
        "image_url": "/static/images/news-8.jpg",
        "is_featured": False,
        "is_breaking": False,
        "views": 6200
    },
    {
        "title": "68 Lakh Accounts Under Ladki Bahin Scheme Closed After Failing to Complete e-KYC",
        "short_description": "The Maharashtra government's ambitious women empowerment scheme faces setback as millions fail to verify their accounts digitally.",
        "content": """<p>In a significant development, the Maharashtra government has closed approximately 68 lakh bank accounts under the Ladki Bahin Yojana after beneficiaries failed to complete their electronic Know Your Customer (e-KYC) verification within the stipulated deadline.</p>
<p>The scheme, launched to provide monthly financial assistance to women from economically weaker sections, had enrolled over 2.5 crore beneficiaries since its inception.</p>
<p>"We had given multiple extensions for e-KYC completion, but these accounts remained unverified," said a senior official from the Women and Child Development Department.</p>
<p>The government has assured that affected women can re-register and complete their verification to resume receiving benefits, with a new deadline set for June 30, 2026.</p>""",
        "category": "Politics",
        "author": "Deepak Kulkarni",
        "image_url": "/static/images/news-9.jpg",
        "is_featured": False,
        "is_breaking": False,
        "views": 11400
    },
    {
        "title": "Govt Approves Shaktipeeth Expressway Redesign — Cost Now ₹1 Lakh Crore",
        "short_description": "The ambitious expressway connecting Nagpur to Goa gets a major redesign with enhanced alignment and expanded scope, pushing costs significantly higher.",
        "content": """<p>The Maharashtra government has approved a comprehensive redesign of the Shaktipeeth Expressway, with the total project cost now estimated at ₹1 lakh crore — almost double the original estimate.</p>
<p>The 808-kilometer expressway, connecting Nagpur to Sindhudurg (near Goa), will now feature a wider alignment with six lanes expandable to eight, along with integrated service roads and rest areas at every 50 kilometers.</p>
<p>"The redesign incorporates feedback from multiple stakeholders and ensures the expressway passes through all major pilgrimage centers of the Shaktipeeth circuit," said the MSRDC chief.</p>
<p>The project is expected to be completed in phases, with the first section between Nagpur and Aurangabad targeted for completion by 2028.</p>""",
        "category": "Mumbai",
        "author": "Anil Desai",
        "image_url": "/static/images/news-10.jpg",
        "is_featured": False,
        "is_breaking": False,
        "views": 9700
    },
    {
        "title": "No More Filthy Beaches: BMC's 24×7 Blitz to Make Mumbai Beaches Spotless",
        "short_description": "Round-the-clock cleaning crews, AI-monitored waste detection, and hefty fines for littering — BMC's comprehensive plan to transform Mumbai's coastline.",
        "content": """<p>The BMC has launched an ambitious beach cleaning program that will deploy round-the-clock cleaning crews, drone-based monitoring, and AI-powered waste detection systems across all of Mumbai's beaches.</p>
<p>The ₹200 crore initiative covers Juhu, Versova, Girgaon Chowpatty, Dadar, Mahim, Gorai, Aksa, and Marve beaches. Each beach will have dedicated teams working in three 8-hour shifts to ensure continuous cleanliness.</p>
<p>"We are committed to giving Mumbaikars beaches they can be proud of," said the BMC Commissioner. "The goal is to achieve Blue Flag certification for at least three Mumbai beaches by 2027."</p>
<p>The program also includes installing underwater trash barriers, setting up recycling stations, and imposing fines of up to ₹25,000 for littering on beaches.</p>""",
        "category": "Mumbai",
        "author": "Sneha Patil",
        "image_url": "/static/images/news-11.jpg",
        "is_featured": False,
        "is_breaking": False,
        "views": 8100
    },
    {
        "title": "Mumbai Real Estate: Luxury Apartment Sells for Record ₹240 Crore in South Mumbai",
        "short_description": "A single apartment in an ultra-luxury tower at Altamount Road sets new record, highlighting the booming premium real estate market in the city.",
        "content": """<p>A luxury penthouse apartment at one of South Mumbai's most prestigious addresses — Altamount Road — has sold for a staggering ₹240 crore, setting a new record for the most expensive residential property transaction in India.</p>
<p>The 12,000-square-foot duplex penthouse, spread across the 65th and 66th floors, offers panoramic views of the Arabian Sea and the city skyline. The deal works out to approximately ₹2 lakh per square foot.</p>
<p>The buyer, reportedly a prominent industrialist, completed the registration in March 2026, paying a stamp duty of approximately ₹14.4 crore.</p>
<p>Real estate experts say the transaction underscores the continued appetite for ultra-luxury properties in Mumbai among India's ultra-high-net-worth individuals.</p>""",
        "category": "Business",
        "author": "Rohit Mehra",
        "image_url": "/static/images/news-12.jpg",
        "is_featured": False,
        "is_breaking": False,
        "views": 14500
    },
    {
        "title": "Nashik's 'Walk of Shame': How a Viral Policing Trend Is Spreading Across Maharashtra",
        "short_description": "The controversial practice of parading accused through streets is dividing public opinion, with rights groups calling it unconstitutional.",
        "content": """<p>A controversial policing trend dubbed the 'Walk of Shame' has been spreading across Maharashtra's cities, sparking intense debate about the boundaries of law enforcement and individual rights.</p>
<p>The practice, which involves publicly parading accused persons through neighborhoods, first gained attention in Nashik before spreading to Pune, Aurangabad, and smaller towns.</p>
<p>"This is a clear violation of the Supreme Court's guidelines on the rights of the accused," said a senior advocate at the Bombay High Court. "No person should be subjected to public humiliation before being convicted."</p>
<p>However, some community leaders have defended the practice, arguing that it serves as a deterrent against crime in areas where conventional policing has failed.</p>
<p>The Maharashtra State Human Rights Commission has taken suo motu cognizance of the issue and issued notices to police departments across the state.</p>""",
        "category": "Politics",
        "author": "Sameer Joshi",
        "image_url": "/static/images/news-13.jpg",
        "is_featured": False,
        "is_breaking": False,
        "views": 7800
    },
    {
        "title": "How a Pink Line on an Android Phone Led to a Mumbai Judge Losing ₹93,000 in Cyber Fraud",
        "short_description": "A sessions court judge fell victim to a sophisticated screen-sharing scam that began with a seemingly innocent technical support call.",
        "content": """<p>In a cautionary tale that highlights the growing sophistication of cyber criminals, a Mumbai sessions court judge lost ₹93,000 after falling victim to a screen-sharing scam that began when a pink line appeared on his Android phone's display.</p>
<p>The judge, whose identity has been withheld, received a call from someone claiming to be from the phone manufacturer's service center. The caller convinced him to install a screen-sharing application to "diagnose" the display issue.</p>
<p>Once the app was installed, the fraudsters gained access to the judge's phone screen, including his banking applications. Within minutes, three unauthorized transactions totaling ₹93,000 were made from his account.</p>
<p>"If a judge with legal expertise can be deceived, imagine how vulnerable ordinary citizens are," said a cyber crime investigator from the Mumbai Police.</p>""",
        "category": "Mumbai",
        "author": "Prachi Desai",
        "image_url": "/static/images/news-14.jpg",
        "is_featured": False,
        "is_breaking": False,
        "views": 13200
    },
    {
        "title": "Maharashtra Launches Rural Health Push to Plug Service Gaps Across Villages",
        "short_description": "New initiative aims to recruit 5,000 healthcare workers and upgrade 2,000 primary health centers in rural Maharashtra.",
        "content": """<p>The Maharashtra government has launched a comprehensive rural healthcare initiative aimed at addressing critical service gaps in the state's villages and semi-urban areas.</p>
<p>The program, with an initial outlay of ₹3,500 crore, will focus on recruiting 5,000 new healthcare workers, upgrading 2,000 primary health centers with modern diagnostic equipment, and establishing telemedicine connectivity in remote areas.</p>
<p>"The pandemic exposed the vulnerabilities of our rural healthcare infrastructure," said the Health Minister. "This initiative is our commitment to ensuring quality healthcare reaches every village in Maharashtra."</p>
<p>Key features include mobile health vans for remote areas, 24/7 emergency response teams, and a health insurance scheme covering up to ₹5 lakh per family.</p>""",
        "category": "India",
        "author": "Gauri Shinde",
        "image_url": "/static/images/news-15.jpg",
        "is_featured": False,
        "is_breaking": False,
        "views": 5600
    },
    {
        "title": "Navi Mumbai to Get 1,00,000-Seater World-Class Cricket Stadium — Work Begins",
        "short_description": "The Maharashtra Cricket Association begins construction of what will be the world's second-largest cricket venue after Ahmedabad's Narendra Modi Stadium.",
        "content": """<p>The Maharashtra Cricket Association (MCA) has officially begun construction work on a massive 1,00,000-seater world-class cricket stadium in Navi Mumbai, which will be the second-largest cricket venue in the world after the Narendra Modi Stadium in Ahmedabad.</p>
<p>The stadium, located near Kharghar, will feature a retractable roof, floodlights conforming to ICC standards, and VIP hospitality suites. The project is estimated to cost ₹4,500 crore.</p>
<p>"This stadium will be a landmark for Indian cricket and will host international matches, IPL games, and potentially ICC tournament finals," said the MCA president.</p>
<p>The facility is expected to be completed by 2029 and will also include indoor practice facilities, a cricket academy, and a sports museum.</p>""",
        "category": "Sports",
        "author": "Amol Karnik",
        "image_url": "/static/images/news-16.jpg",
        "is_featured": False,
        "is_breaking": True,
        "views": 21000
    },
    {
        "title": "Mumbai Rains: IMD Predicts Early Monsoon Arrival by June First Week",
        "short_description": "The India Meteorological Department forecasts an earlier-than-usual monsoon onset for Mumbai, advising civic agencies to prepare in advance.",
        "content": """<p>The India Meteorological Department (IMD) has predicted that the southwest monsoon is likely to arrive in Mumbai by the first week of June — about 5-7 days earlier than its usual onset date of June 11.</p>
<p>"Current ocean conditions, including favorable La Niña patterns and warmer Arabian Sea surface temperatures, suggest an early and vigorous monsoon this year," said the IMD director.</p>
<p>The BMC has been put on alert and has accelerated its pre-monsoon preparations, including desilting of storm water drains, trimming of trees, and deployment of high-capacity pumps at chronic flooding spots.</p>
<p>IMD has also predicted that Mumbai is likely to receive above-average rainfall this monsoon season, with the total estimated at 2,500-2,700 mm against the normal of 2,350 mm.</p>""",
        "category": "Mumbai",
        "author": "Nilesh Desai",
        "image_url": "/static/images/news-17.jpg",
        "is_featured": False,
        "is_breaking": False,
        "views": 10300
    },
    {
        "title": "Mumbai Train Assault: GRP Tracks Down Woman, Minor Son in Viral Attack on Disabled Passengers",
        "short_description": "Kurla Government Railway Police identifies and detains the duo seen in viral video attacking passengers with disabilities on a local train.",
        "content": """<p>The Kurla Government Railway Police (GRP) has tracked down a woman and her minor son who were seen in a viral video assaulting passengers with disabilities on a Mumbai local train.</p>
<p>The video, which went viral on social media, showed the woman and her teenage son verbally abusing and physically attacking two visually impaired passengers for allegedly occupying seats in the compartment.</p>
<p>"We identified the accused through CCTV footage at Kurla station and mobile number records," said the Senior Police Inspector at Kurla GRP. "The woman has been arrested and her son has been referred to the Juvenile Justice Board."</p>
<p>The incident has renewed calls for better security on Mumbai's local trains, which carry over 75 lakh passengers daily.</p>""",
        "category": "Mumbai",
        "author": "Rajiv Khanna",
        "image_url": "/static/images/news-18.jpg",
        "is_featured": False,
        "is_breaking": False,
        "views": 16700
    },
    {
        "title": "6 Years Later, BMC's 'Smart Parking' Project to Finally Hit the Road",
        "short_description": "The long-delayed digital parking management system will launch in South Mumbai, allowing drivers to book and pay for parking spots via app.",
        "content": """<p>After six years of delays, the BMC's ambitious 'Smart Parking' project is finally set to become operational, starting with a pilot launch in South Mumbai's Fort and Colaba areas.</p>
<p>The system will allow drivers to find, book, and pay for on-street parking spots through a dedicated mobile application. Sensors embedded in each parking space will track occupancy in real time.</p>
<p>"We have installed sensors in over 3,000 parking spaces in the pilot zone," said the BMC official overseeing the project. "The app will show available spots, guide drivers to them, and handle payments digitally."</p>
<p>Parking rates will be dynamic, varying based on demand and time of day — a first for any Indian city. The system is expected to reduce illegal parking and traffic congestion significantly.</p>""",
        "category": "Mumbai",
        "author": "Sunita More",
        "image_url": "/static/images/news-19.jpg",
        "is_featured": False,
        "is_breaking": False,
        "views": 7900
    },
    {
        "title": "Freedom of Expression Must Be Protected Even If Criticism Hurts: Justice Oka",
        "short_description": "Supreme Court Justice B.V. Nagarathna and Justice Oka emphasize the importance of tolerating dissent in a democracy at a Mumbai event.",
        "content": """<p>"To preserve freedom of expression, we must learn to tolerate criticism, even when it is harsh and uncomfortable," said Supreme Court Justice Abhay Shreeniwas Oka at a legal conference in Mumbai.</p>
<p>Speaking at the Bombay Bar Association's annual lecture, Justice Oka emphasized that a healthy democracy requires robust debate and that courts must remain vigilant against attempts to silence dissent.</p>
<p>"History teaches us that the suppression of free speech has always preceded authoritarianism," he said. "The judiciary has a sacred duty to protect this fundamental right."</p>
<p>He also spoke about the challenges of balancing free expression with the right to privacy and reputation, calling for nuanced judicial approaches rather than blanket restrictions.</p>""",
        "category": "India",
        "author": "Advocate Arun Mehta",
        "image_url": "/static/images/news-20.jpg",
        "is_featured": False,
        "is_breaking": False,
        "views": 4800
    },
    {
        "title": "Maharashtra Sets Up New Panel on Scheduled Castes Quota Split — Badar Report Tabled",
        "short_description": "The state legislature tables the Badar Committee report on sub-categorization of SC reservations and forms a new panel for implementation.",
        "content": """<p>The Maharashtra government has set up a new panel to examine the implementation of sub-categorization of Scheduled Castes reservations, following the tabling of the Badar Committee report in the state legislature.</p>
<p>The new committee, headed by a retired High Court judge, will study the recommendations and suggest a roadmap for equitable distribution of reservation benefits among different SC sub-groups.</p>
<p>Social justice activists have welcomed the move, saying that certain SC sub-communities have historically been underrepresented in the benefits of reservation.</p>""",
        "category": "Politics",
        "author": "Manoj Pawar",
        "image_url": "/static/images/news-21.jpg",
        "is_featured": False,
        "is_breaking": False,
        "views": 3200
    },
]

def seed_database():
    with app.app_context():
        # Clear existing articles
        Article.query.delete()
        db.session.commit()

        for i, data in enumerate(SAMPLE_ARTICLES):
            slug = data['title'].lower().strip()
            import re
            slug = re.sub(r'[^\w\s-]', '', slug)
            slug = re.sub(r'[\s_-]+', '-', slug)
            slug = re.sub(r'^-+|-+$', '', slug)

            article = Article(
                title=data['title'],
                slug=slug,
                content=data['content'],
                short_description=data['short_description'],
                category=data['category'],
                author=data['author'],
                image_url=data['image_url'],
                is_featured=data.get('is_featured', False),
                is_breaking=data.get('is_breaking', False),
                views=data.get('views', 0),
                publish_date=datetime.utcnow() - timedelta(hours=random.randint(1, 72)),
                status='published'
            )
            db.session.add(article)

        db.session.commit()
        print(f"✅ Seeded {len(SAMPLE_ARTICLES)} articles successfully!")
        print(f"📝 Admin login: username='admin', password='admin123'")

if __name__ == '__main__':
    seed_database()
