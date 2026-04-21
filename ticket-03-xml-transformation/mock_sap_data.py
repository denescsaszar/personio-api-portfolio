MOCK_SAP_XML = """<?xml version="1.0" encoding="UTF-8"?>
<Applicants>

    <!-- Software Engineers -->
    <Applicant id="1">
        <FirstName>Maria</FirstName>
        <LastName>Schmidt</LastName>
        <EmailAddress>maria.schmidt@siemens.de</EmailAddress>
        <JobTitle>Software Engineer</JobTitle>
        <ApplicationDate>2026-01-10</ApplicationDate>
        <RecruitingStatus>open</RecruitingStatus>
        <SourceType>Karriereseite</SourceType>
    </Applicant>

    <Applicant id="2">
        <FirstName>Klaus</FirstName>
        <LastName>Müller</LastName>
        <EmailAddress>klaus.mueller@siemens.de</EmailAddress>
        <JobTitle>Software Engineer</JobTitle>
        <ApplicationDate>2026-01-22</ApplicationDate>
        <RecruitingStatus>hired</RecruitingStatus>
        <SourceType>LinkedIn</SourceType>
    </Applicant>

    <Applicant id="3">
        <FirstName>Sarah</FirstName>
        <LastName>Weber</LastName>
        <EmailAddress>sarah.weber@siemens.de</EmailAddress>
        <JobTitle>Software Engineer</JobTitle>
        <ApplicationDate>2026-02-05</ApplicationDate>
        <RecruitingStatus>rejected</RecruitingStatus>
        <SourceType>Empfehlung</SourceType>
    </Applicant>

    <!-- DevOps Engineers -->
    <Applicant id="4">
        <FirstName>Thomas</FirstName>
        <LastName>Bauer</LastName>
        <EmailAddress>thomas.bauer@siemens.de</EmailAddress>
        <JobTitle>DevOps Engineer</JobTitle>
        <ApplicationDate>2026-02-14</ApplicationDate>
        <RecruitingStatus>hired</RecruitingStatus>
        <SourceType>Karriereseite</SourceType>
    </Applicant>

    <Applicant id="5">
        <FirstName>Anna</FirstName>
        <LastName>Hoffmann</LastName>
        <EmailAddress>anna.hoffmann@siemens.de</EmailAddress>
        <JobTitle>DevOps Engineer</JobTitle>
        <ApplicationDate>2026-03-01</ApplicationDate>
        <RecruitingStatus>open</RecruitingStatus>
        <SourceType>LinkedIn</SourceType>
    </Applicant>

    <!-- Product Manager -->
    <Applicant id="6">
        <FirstName>Felix</FirstName>
        <LastName>Richter</LastName>
        <EmailAddress>felix.richter@siemens.de</EmailAddress>
        <JobTitle>Product Manager</JobTitle>
        <ApplicationDate>2026-03-10</ApplicationDate>
        <RecruitingStatus>open</RecruitingStatus>
        <SourceType>Empfehlung</SourceType>
    </Applicant>

    <Applicant id="7">
        <FirstName>Laura</FirstName>
        <LastName>Braun</LastName>
        <EmailAddress>laura.braun@siemens.de</EmailAddress>
        <JobTitle>Product Manager</JobTitle>
        <ApplicationDate>2026-03-18</ApplicationDate>
        <RecruitingStatus>open</RecruitingStatus>
        <SourceType>Karriereseite</SourceType>
    </Applicant>

    <!-- Data Analyst -->
    <Applicant id="8">
        <FirstName>Nico</FirstName>
        <LastName>Koch</LastName>
        <EmailAddress>nico.koch@siemens.de</EmailAddress>
        <JobTitle>Data Analyst</JobTitle>
        <ApplicationDate>2026-04-01</ApplicationDate>
        <RecruitingStatus>open</RecruitingStatus>
        <SourceType>LinkedIn</SourceType>
    </Applicant>

    <!-- FEHLERHAFTE DATENSÄTZE (fehlende Pflichtfelder) -->
    <Applicant id="9">
        <FirstName>Peter</FirstName>
        <LastName>Lang</LastName>
        <EmailAddress></EmailAddress>
        <JobTitle></JobTitle>
        <ApplicationDate>2026-04-05</ApplicationDate>
        <RecruitingStatus>open</RecruitingStatus>
        <SourceType>Karriereseite</SourceType>
    </Applicant>

    <Applicant id="10">
        <FirstName>Julia</FirstName>
        <LastName></LastName>
        <EmailAddress>julia@siemens.de</EmailAddress>
        <JobTitle>HR Manager</JobTitle>
        <ApplicationDate>2026-04-10</ApplicationDate>
        <RecruitingStatus>open</RecruitingStatus>
        <SourceType>LinkedIn</SourceType>
    </Applicant>

</Applicants>
"""