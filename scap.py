from bs4 import BeautifulSoup

url = "Kempinski Hotel Bristol Berlin, Germany - Booking.com (1).html"

page = open(url, encoding="utf8")

soup = BeautifulSoup(page, 'html.parser')


def red():
    global red_head
    red_head = soup.find(id="hp_hotel_name").text.strip()
    global red_address
    red_address = soup.find(id="hp_address_subtitle").text.strip()
red()

def purple():

    purple_summary = soup.find_all(p="", id= "summary", name = "div")
    global new_desc
    new_desc = []
    for purple in purple_summary:
        purple = purple.select("p")
        for p in purple:
            p = p.getText().strip()
            new_desc.append(p)
purple()

def pink():
    global pink_points
    pink_points = soup.find(class_="js--hp-scorecard-scoreword").text.strip()
    global pink_rating
    pink_rating = soup.find(class_="average js--hp-scorecard-scoreval").text.strip()
    global pink_review_count
    pink_review_count = soup.find(class_="trackit score_from_number_of_reviews").text.strip()
pink()

Alternative_hotels = {} #Dictionary of Alternative Hotels in Yellow Box
def func_yellow():

    yellow_desc = soup.find_all(class_="hp_compset_description")
    yellow_name = soup.find_all(class_="althotel_link")
    yellow_message = soup.find_all(class_="altHotels_most_recent_booking urgency_message_red")
    yellow_review = soup.find_all(class_="trackit score_from_number_of_reviews")
    yellow_review_details = soup.find_all(class_="big_review_score_detailed js-big_review_score_detailed ind_rev_total hp_review_score")

    alt_hotel_desc = []
    alt_hotel_name= []
    alt_hotel_message = []
    alt_hotel_review = []
    alt_hotel_review_details = []
    for y in yellow_desc:
        y = y.getText().strip()
        alt_hotel_desc.append(y)

    for y in yellow_name:
        y = y.getText().strip()
        alt_hotel_name.append(y)

    for y in yellow_message:
        y = y.getText().strip()
        alt_hotel_message.append(y)

    for y in yellow_review:
        y = y.getText().strip()
        alt_hotel_review.append(y)

    for y in yellow_review_details:
        y = y.getText().strip()
        y = y.replace("\n", " ")
        alt_hotel_review_details.append(y)

    alt_hotel_review_details.pop(0)
    alt_hotel_review.pop(0)


    Alternative_hotels = {
        "Hotel_name": alt_hotel_name,
        "Hotel_description": alt_hotel_desc,
        "Hotel_message": alt_hotel_message,
        "Hotel_review" : alt_hotel_review,
        "Hotel_review_details":alt_hotel_review_details,
            }
    return Alternative_hotels

Alternative_hotels = func_yellow()

def green():
    # green_heading = soup.find(class_="hp_last_booking").text
    green_table = soup.find_all(class_="ftd")
    global g
    g = []
    for green in green_table:
        green = green.text.strip()
        g.append(green)
green()

answer = {}
answer = {
    "hotel_name": red_head,
    "address": red_address,
    " Review points": pink_points+" "+pink_rating,
    "Number of reviews": pink_review_count,
    "Description": new_desc,
    "Room categories": g,
    "Alternative_hotels": Alternative_hotels,
}

print(answer)