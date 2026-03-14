# Solidary Mothers

#### Video Demo: https://youtu.be/hgaaN9prujo
#### Description:

Solidary Mothers is a web-based platform designed to connect mothers who want to donate baby items with mothers in need. As someone preparing for motherhood myself, I realized how expensive baby essentials can be and how many families struggle to afford everything their newborns need. At the same time, many mothers have gently used items sitting unused after their children outgrow them. Solidary Mothers bridges this gap by creating a supportive community where mothers help other mothers.

## Project Overview

The platform allows users to browse available donations, request specific items they need, donate items they no longer use, and access a comprehensive baby essentials checklist. All features are designed with simplicity and accessibility in mind, ensuring that mothers from all backgrounds can easily navigate and use the platform.

## Features

### 1. Browse Available Donations
The Items page displays all currently available donations in a clean, filterable interface. Users can search by:
- *Category* (clothing, toys, furniture, feeding supplies, etc.)
- *Location* (city and state)
- *Condition* (new, like new, good, fair)

Each listing includes a photo, detailed description, and the donor's contact information. I chose to include SMS contact functionality to make communication between donors and recipients as seamless as possible, recognizing that text messaging is often more accessible than email for busy parents.

### 2. Request Items
Mothers who need specific items can submit requests through a simple form. These requests are stored in the database and displayed publicly, allowing potential donors to see what families in their community need most. This feature was inspired by the idea of "reverse donations" - instead of only showing what's available, we also highlight what's needed.

### 3. Donate Items
The donation form allows users to list items they want to give away. I included the option to upload photos because visual representation significantly increases the likelihood of successful matches. The form collects essential information like item category, gender suitability (for clothing), condition, and detailed descriptions.

### 4. Baby Essentials Checklist
This educational resource helps new and expecting mothers understand what items are truly essential. The checklist is organized by category (nursery, feeding, clothing, etc.) and serves both as a planning tool and as inspiration for what to donate or request.

### 5. About Page
This page explains the mission and vision behind Solidary Mothers, emphasizing community support and the belief that every baby deserves a good start in life.

## Technical Implementation

### Backend
The application is built with *Python* and *Flask*, chosen for its simplicity and extensive documentation. Flask's lightweight nature made it ideal for a project of this scope while still providing all necessary functionality.

The database uses *SQLite* (envoval.db) to store:
- Donation listings (item details, donor information, status)
- Requests from mothers in need
- Baby checklist items

I chose SQLite because it requires no separate database server, making the project easy to deploy and maintain while still providing full relational database capabilities.

### Frontend
The user interface combines *HTML, **CSS, and **JavaScript* to create an engaging, responsive experience. I made several deliberate design choices:

*Color Scheme*: Soft pastel colors (pink, yellow, mint green) create a warm, welcoming atmosphere that feels nurturing and approachable - essential for a platform focused on motherhood and community support.

*Animations*: Subtle floating baby-themed emojis and smooth transitions make the interface feel alive and joyful without being overwhelming or distracting.

*Mobile-First Design*: Given that many mothers will access the platform on their phones while multitasking, I prioritized mobile responsiveness throughout the design process.

### Form Handling
All forms include comprehensive validation to ensure data quality. Required fields are clearly marked, and users receive immediate feedback if they submit incomplete information.

## Design Decisions

### Why SMS Instead of In-Platform Messaging?
I chose to facilitate direct SMS contact between donors and recipients rather than building an in-platform messaging system for several reasons:
1. *Immediacy*: Text messages are typically read within minutes
2. *Familiarity*: Everyone knows how to text
3. *Accessibility*: No need to create accounts or remember to check another inbox
4. *Simplicity*: Reduced development complexity while maintaining functionality

### Why Public Requests?
Displaying requests publicly (rather than matching them privately) creates transparency and allows donors to see the real needs in their community, which can be more motivating than simply browsing available items.

### Database Structure
I designed the database with flexibility in mind. The donations table tracks status (available, donated, deleted) so items can be soft-deleted rather than permanently removed, preserving data for potential analytics about platform usage and community impact.

## How to Run

1. Clone the repository
2. Navigate to the project directory
3. Install dependencies: pip install -r requirements.txt
4. Run the application: flask run
5. Open your browser to http://127.0.0.1:5000

## Future Enhancements

Given more time, I would add:
- User accounts with donation/request history
- Email notifications when requested items become available
- Geographic filtering to show nearby donations first
- Success stories section to celebrate community impact
- Multi-language support for non-English speaking communities

## Conclusion

Solidary Mothers represents my belief that technology should serve human connection and community support. While the platform is currently a prototype with sample data, it demonstrates how a simple web application can facilitate meaningful real-world impact. Creating this project deepened my understanding of full-stack development while allowing me to build something that could genuinely help families in need.

---

*Project by Leticia Sanchez*  
CS50x Final Project - 2026
