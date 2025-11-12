# Dataset Information

## Required Datasets

### 1. Customer Social Profiles

- **Filename:** `customer_social_profiles.csv`
- **Download Link:** [TO BE ADDED]
- **Description:** Contains customer information from social media platforms
- **Expected Columns:** (to be determined after viewing)
  - Customer ID
  - Social media metrics
  - Demographic information
  - Engagement data
  - etc.

**Download Instructions:**

```bash
# Navigate to data/raw directory
cd data/raw/

# Download the file (example)
# wget [LINK] -O customer_social_profiles.csv
# or manually download and place here
```

---

### 2. Customer Transactions

- **Filename:** `customer_transactions.csv`
- **Download Link:** [TO BE ADDED]
- **Description:** Contains customer purchase history and transaction data
- **Expected Columns:** (to be determined after viewing)
  - Customer ID
  - Transaction ID
  - Product information
  - Purchase date
  - Amount
  - etc.

**Download Instructions:**

```bash
# Navigate to data/raw directory
cd data/raw/

# Download the file (example)
# wget [LINK] -O customer_transactions.csv
# or manually download and place here
```

---

## Dataset Status

| Dataset                      | Downloaded | Verified | Location    |
| ---------------------------- | ---------- | -------- | ----------- |
| customer_social_profiles.csv | ⬜         | ⬜       | `data/raw/` |
| customer_transactions.csv    | ⬜         | ⬜       | `data/raw/` |

---

## Team Data Collection Status

### Facial Images (12 total required)

| Team Member | Neutral | Smile | Surprised | Status |
| ----------- | ------- | ----- | --------- | ------ |
| Mitali      | ⬜      | ⬜    | ⬜        | 0/3    |
| Blessing    | ⬜      | ⬜    | ⬜        | 0/3    |
| Liliane     | ⬜      | ⬜    | ⬜        | 0/3    |
| Mwai        | ⬜      | ⬜    | ⬜        | 0/3    |

**Total:** 0/12

---

### Audio Recordings (8 total required)

| Team Member | "Yes, approve" | "Confirm transaction" | Status |
| ----------- | -------------- | --------------------- | ------ |
| Mitali      | ⬜             | ⬜                    | 0/2    |
| Blessing    | ⬜             | ⬜                    | 0/2    |
| Liliane     | ⬜             | ⬜                    | 0/2    |
| Mwai        | ⬜             | ⬜                    | 0/2    |

**Total:** 0/8

---

## Image Collection Guidelines

### Requirements:

- **Format:** JPG or PNG
- **Resolution:** At least 640x480 pixels (higher is better)
- **Lighting:** Well-lit, avoid shadows on face
- **Background:** Plain background preferred
- **Face:** Clearly visible, front-facing
- **Expressions:**
  - **Neutral:** Relaxed face, no smile, passport-style
  - **Smile:** Natural smile, teeth showing optional
  - **Surprised:** Wide eyes, raised eyebrows, open mouth

### Naming Convention:

```
{firstname}_neutral.jpg
{firstname}_smile.jpg
{firstname}_surprised.jpg
```

**Example:**

```
mitali_neutral.jpg
mitali_smile.jpg
mitali_surprised.jpg
```

### How to Submit:

1. Take photos (use phone or webcam)
2. Rename files according to convention
3. Place in `data/images/` directory
4. Commit to GitHub or share via Google Drive/Dropbox

---

## Audio Recording Guidelines

### Requirements:

- **Format:** WAV (preferred) or MP3
- **Sample Rate:** 16 kHz or 44.1 kHz
- **Bit Depth:** 16-bit or higher
- **Duration:** 2-3 seconds per phrase
- **Quality:** Clear audio, minimal background noise
- **Volume:** Speak at normal conversational level

### Phrases to Record:

1. **Phrase 1:** "Yes, approve"
2. **Phrase 2:** "Confirm transaction"

### Naming Convention:

```
{firstname}_approve.wav
{firstname}_confirm.wav
```

**Example:**

```
mitali_approve.wav
mitali_confirm.wav
```

### Recording Options:

1. **Phone:** Use voice recorder app, export as WAV or MP3
2. **Computer:** Use Audacity (free software)
3. **Online:** Use online voice recorder tools

### How to Submit:

1. Record both phrases
2. Export as WAV files
3. Rename according to convention
4. Place in `data/audio/` directory
5. Commit to GitHub or share via Google Drive/Dropbox (if files too large)

---

## Data Verification Checklist

Before starting analysis, verify:

### Tabular Data:

- [ ] Both CSV files downloaded
- [ ] Files open without errors
- [ ] No obvious corruption
- [ ] Column names are readable
- [ ] At least some rows of data present

### Image Data:

- [ ] All 12 images collected
- [ ] Files open and display correctly
- [ ] Faces are clearly visible
- [ ] Consistent quality across images
- [ ] Proper naming convention followed

### Audio Data:

- [ ] All 8 audio files collected
- [ ] Files play without errors
- [ ] Voice is clearly audible
- [ ] Minimal background noise
- [ ] Proper naming convention followed

---

## Troubleshooting

### Dataset Download Issues:

**Problem:** Links not working  
**Solution:** Contact instructor immediately

**Problem:** Files too large to download  
**Solution:** Check if datasets are split into parts or compressed

**Problem:** Access denied  
**Solution:** Verify you're logged into course platform

### Image Collection Issues:

**Problem:** Poor lighting  
**Solution:** Take photos near window (natural light) or under bright indoor light

**Problem:** File size too large  
**Solution:** Resize images to 1024x768 or compress without losing quality

**Problem:** Can't make expressions  
**Solution:** Look at reference images online for guidance

### Audio Recording Issues:

**Problem:** Too much background noise  
**Solution:** Record in quiet room, close windows, turn off fans

**Problem:** Voice too quiet  
**Solution:** Move closer to microphone, speak slightly louder

**Problem:** Can't save as WAV  
**Solution:** Record as MP3 and convert using Audacity or online converter

---

## Next Steps

1. **Mitali:** Share dataset links when received
2. **All Team Members:**
   - Download datasets to `data/raw/`
   - Collect personal images
   - Record audio samples
   - Verify all files
3. **Team Lead:** Confirm all data collected before starting analysis

---

## Contact

If you have issues collecting data or accessing datasets:

- **GitHub Issues:** [Repository Issues Page]
- **Team Chat:** [Platform]
- **Email:** [Team email list]

---

_Last Updated: November 11, 2025_  
_Status: Awaiting dataset links from instructor_
