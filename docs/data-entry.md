# Registration Data Entry Standard Operating Procedure 

This guide provides step-by-step instructions for manually migrating user registration data from the web form into the structured Excel database. 

**IMPORTANT DATABASE RULE:** Data must be entered in a specific order due to relational dependencies. 

---

## Step 1: Supervisor Data Entry (`supervisors` sheet)

Check the registration form for the user's supervisor details.

1. **Search Existing:** First, search the `supervisors` sheet using the supervisor's email to avoid duplicates.
2. **Add New (If not found):**
   * **`supervisor_id`**: Assign the next sequential integer (e.g., if the last row is 127, use `128`).
   * **`full_name`**: Extract from the supervisor name field.
   * **`email`**: Extract from the supervisor email field.

*Note down the `supervisor_id` as you will need it for Step 2.*

---

## Step 2: Student Data Entry (`students` sheet)

Check the registration form for the user details. Search the `students` sheet using the user's email to avoid duplicates.

* **`student_id`**: Assign the next sequential integer (e.g., if the last row is 608, use `609`).
* **`full_name`**: User's full name.
* **`email`**: User's email address.
* **`gender`**: Enter exactly as `male` or `female`.
* **`it_background`**: Enter exactly as `TRUE` or `FALSE`.
* **`experience_min_years`**: Extract the lower bound of their experience range (e.g., for "Nil" or "<1 year", enter `0`. For "1-5 years", enter `1`. For ">5  years", enter `5`).
* **`experience_max_years`**: Extract the upper bound of their experience range (e.g., for "Nil", enter `0`.  For "<1 year", enter `1`. For "1-5 years", enter `5`. For ">5  years", enter `100`).
* **`sector`**: Enter exactly as `Government`, `Private`, or `Student`.
* **`supervisor_id`**: Enter the integer ID obtained from Step 1. Leave blank ONLY if not applicable.
* **`company`**: Company/Agency/University name.
* **`job_title`**: Position name.
* **`country`**: 2-letter country code (e.g., `MY` for Malaysia).  Use `UNKNOWN` only if not applicable.
* **`phone`**: Include the country code (e.g., `+60123456789`). Use `NAN` only if not applicable.

*Note down the new `student_id` for Step 4.*

---

## Step 3: Identify the Session (`courses` sheet & `sessions` sheet)

You do not need to add new rows here, but you must find the correct `session_id` for the enrollment.

1. Look at the course requested by the user in the registration form.
2. Open `courses` sheet to confirm the `course_id`.
3. Open `sessions` sheet and locate the exact row that matches both the `course_id` and the requested date/time (`start_datetime`) to confirm the `session_id`.

*Note down the `session_id` from that row for Step 4.*



You must link the student to a specific session. If the information is missing, you must manually update the reference tables.

1.  Check `courses` sheet: Search for the course name. If not found, assign a new Primary Key  (last ID + 1) and enter the `course_name`.
2.  Check `sessions` sheet: Find the row matching the `course_id` and the requested date/time.
    1.  If no matching session exists, create a new one.
    2.  Ensure the Foreign Key (`course_id`) correctly points to the corresponding course.


---

## Step 4: Enrollment Data Entry (`enrollments` sheet)

Link the student to their requested course session.

* **`enrollment_id`**: Assign the next sequential integer.
* **`student_id`**: Enter the ID generated in Step 2.
* **`session_id`**: Enter the ID identified in Step 3.
* **`reg_date`**: Enter the date the registration form was submitted (Format: `YYYY-MM-DD 00:00:00`).
* **`completed`**: Default to `FALSE`.
* **`payment_status`**: Enter exactly as `PENDING` or `PAID`.
* **`exception`**: Enter specific tags if applicable, otherwise leave blank.
