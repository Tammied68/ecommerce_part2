# eCommerce Application – Part 2  
## Twitter (X) API Integration

This project implements the requirements for eCommerce Application Part 2, including:

- Creating a Twitter (X) Developer Account  
- Configuring API keys and OAuth 1.0a credentials  
- Integrating the Twitter API into the Django application  
- Automatically sending tweets when:
  - A new store is created
  - A new product is created
- Attaching media (store logos or product images) when available

---

## Important Note About Tweet Posting

As of 2024–2026, **Twitter/X no longer provides complimentary write access** on the free developer tier.  
This means:

- Free developer accounts **cannot post tweets**
- Attempts to tweet return **403 Forbidden**
- This is a platform restriction, not a code error

I documented this limitation in my code and verified that my OAuth credentials, permissions, and integration logic are correct.

If upgraded API access were available, the existing code would successfully post tweets.

---

## Project Structure

- `stores/` – Store model, serializer, view, and tweet-on-create logic  
- `products/` – Product model, serializer, view, and tweet-on-create logic  
- `services/twitter_service.py` – Handles authentication and tweet requests  
- `product_images/` – Uploaded product images  
- `store_logos/` – Uploaded store logos  
- `sticky_github.txt` – Contains the link to this repository

---

## How to Test

1. Create a new store → triggers tweet logic  
2. Create a new product → triggers tweet logic  
3. Check console logs for:
   - Tweet attempt
   - API response
   - 403 Forbidden (expected on free tier)

The logic executes correctly even though the platform blocks posting.

---

## Notes

All API keys are stored in a `.env` file and **not included** in this repository for security.
