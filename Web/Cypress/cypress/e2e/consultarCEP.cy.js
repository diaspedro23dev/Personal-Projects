/// <reference types="cypress" />

describe("Testes automaticos da API consulta CEP", ()=>{
    it('Consulta de um CEP válido', ()=>{
        cy.request({
            method: 'GET',
            url: 'https://viacep.com.br/ws/80420200/json/',
            failOnStatusCode: false
        }).as('response')
        cy.get('@response').should((response)=>{
            expect(response.status).to.equal(200),
            expect(response.body.cep).to.equal('80420-200')
            expect(response.body.logradouro).to.equal('Rua Brigadeiro Franco')
            expect(response.body.complemento).to.equal('de 1395/1396 a 2049/2050')
            expect(response.body.bairro).to.equal('Centro')
            expect(response.body.localidade).to.equal('Curitiba')
            expect(response.body.uf).to.equal('PR')
            expect(response.body.ibge).to.equal('4106902')
            expect(response.body.gia).to.equal('')
            expect(response.body.ddd).to.equal('41')
            expect(response.body.siafi).to.equal('7535')
        })
    })

})