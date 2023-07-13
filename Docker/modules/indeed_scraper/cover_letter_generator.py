import openai

openai.api_key = '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'

def generate_cover_letter(resume_text, job_description):
    prompt = "Write a cover letter for the job with the following information:\n\nResume Text: {}\n\nJob Description: {}".format(
        resume_text, job_description
    )

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=500,
        temperature=0.7,
        top_p=0.9,
    )

    return response.choices[0].text.strip()


